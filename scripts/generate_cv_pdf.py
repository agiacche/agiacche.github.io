#!/usr/bin/env python3
"""
Generate the downloadable CV PDF from the built site's print page.

This does NOT re-derive any CV content itself: the print page it screenshots
(/cv/print/) is rendered by Jekyll from the exact same data as the on-site CV
(_data/cv.yml, _publications/, _teaching*/, _events/ - see _includes/cv-content.html),
so there is nothing to keep in sync here beyond "build the site, then run this".

Usage:
    bundle exec jekyll build            # (or the apt/local-dev equivalent)
    python3 scripts/generate_cv_pdf.py

Requires: playwright (with the Chromium browser installed) - `pip install
playwright && playwright install chromium`.

What it does:
    1. Serves the already-built site (default: ./_site) over plain HTTP on
       localhost, so relative asset paths behave exactly as they do on the
       real GitHub Pages server - a mistake here (e.g. opening the file
       directly as a file:// URL) is exactly what silently breaks CSS/JS
       loading and relative links.
    2. Opens /cv/print/ in headless Chromium. That page's <head> sets
       <base href="https://.../"> from site.url (see _layouts/cv-print.html),
       so every relative link (theses, teaching pages, event pages) resolves
       to a real, absolute, clickable production URL in the output PDF -
       regardless of the fact that this script is serving the page from
       localhost.
    3. Waits for MathJax to finish typesetting any inline math in
       publication/thesis titles (best-effort: if MathJax can't load at all,
       e.g. no network access, this warns and continues rather than failing
       the whole build - the PDF will just show raw TeX source in that case).
    4. Prints the page to PDF. Page size/margins come from the page's own
       `@page` CSS rule (assets/css/cv-print.scss) via prefer_css_page_size,
       so A4 + margins are defined in exactly one place.
    5. Writes the result to files/giacchetto_cv_en.pdf (the stable URL the
       rest of the site already links to) and does a couple of basic sanity
       checks on the file it just wrote.
"""

import argparse
import functools
import http.server
import sys
import threading
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SITE_DIR = REPO_ROOT / "_site"
DEFAULT_OUTPUT = REPO_ROOT / "files" / "giacchetto_cv_en.pdf"
PRINT_PATH = "/cv/print/"


def serve_site(site_dir: Path, port: int) -> http.server.ThreadingHTTPServer:
    """Serve `site_dir` over plain HTTP in a background thread."""
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(site_dir))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def wait_for_mathjax(page, timeout_ms: int = 15000) -> None:
    """Best-effort wait for MathJax to finish typesetting. Never raises."""
    try:
        page.wait_for_function("window.MathJax !== undefined", timeout=timeout_ms)
        page.evaluate(
            """async () => {
                if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
                    await window.MathJax.startup.promise;
                }
            }"""
        )
    except Exception as exc:  # noqa: BLE001 - deliberately tolerant, see module docstring
        print(f"warning: MathJax did not finish loading/typesetting ({exc}); "
              f"the PDF may show raw TeX source instead of rendered math.", file=sys.stderr)


def generate(site_dir: Path, output: Path, port: int, base_url_override: str | None) -> None:
    from playwright.sync_api import sync_playwright

    if not site_dir.is_dir():
        raise SystemExit(f"Site directory not found: {site_dir}\n"
                          f"Build the site first (e.g. `bundle exec jekyll build`).")

    server = serve_site(site_dir, port)
    try:
        url = base_url_override or f"http://127.0.0.1:{port}{PRINT_PATH}"
        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--no-sandbox"])
            page = browser.new_page()
            page.goto(url, wait_until="networkidle")
            wait_for_mathjax(page)

            output.parent.mkdir(parents=True, exist_ok=True)
            page.pdf(path=str(output), print_background=True, prefer_css_page_size=True)

            browser.close()
    finally:
        server.shutdown()

    sanity_check(output)


def sanity_check(pdf_path: Path) -> None:
    size = pdf_path.stat().st_size
    if size < 5_000:
        raise SystemExit(f"Generated PDF looks suspiciously small ({size} bytes): {pdf_path}")
    with open(pdf_path, "rb") as f:
        head = f.read(5)
    if head != b"%PDF-":
        raise SystemExit(f"Generated file does not look like a PDF: {pdf_path}")
    print(f"Wrote {pdf_path} ({size / 1024:.0f} KiB)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--site-dir", type=Path, default=DEFAULT_SITE_DIR,
                         help=f"Path to the already-built site (default: {DEFAULT_SITE_DIR})")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT,
                         help=f"Where to write the PDF (default: {DEFAULT_OUTPUT})")
    parser.add_argument("--port", type=int, default=8123, help="Local port to serve the built site on")
    parser.add_argument("--base-url", default=None,
                         help="Fetch the print page from this URL instead of serving --site-dir locally "
                              "(e.g. to generate against an already-deployed site)")
    args = parser.parse_args()

    generate(args.site_dir, args.output, args.port, args.base_url)


if __name__ == "__main__":
    main()
