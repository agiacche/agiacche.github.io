# Maintaining this site

Practical notes for keeping this site up to date. (For generic Academic
Pages/Jekyll setup, see `README.md`.)

## Adding a new publication

Publications have a single canonical representation, used by both the
`/publications/` page and the CV (`/cv/`, and the CV PDF): a file in
`_publications/`.

1. Copy an existing file in `_publications/` as a starting point (e.g. the
   most recent one) and rename it, conventionally after the arXiv id
   (`2501-12345.md`).
2. Fill in the front matter. The fields actually used are:
   - `title`, `coauthors`, `year`, `date` (used for sorting - the exact day
     doesn't matter, but keep the year/month right)
   - `category`: `"published"`, `"preprint"`, or `"book"` (controls how the
     venue line renders - `"preprint"` just shows "Preprint")
   - `journal`, `volume`, `issue`, `series`, `note` - only used when
     `category` is `"published"`/`"book"`
   - `arxiv` (just the id, e.g. `"2501.12345"`), `doi`, `open` (a direct
     open-access URL), `git` (a `user/repo` GitHub path), `pdf` (a local
     file under `files/`), `slides` - all optional, each one shows as a
     labelled link (arXiv / DOI / PDF / Open access / Code / Slides)
   - `permalink`: **must be unique** - `/publications/<same-id-as-filename>`.
     A duplicated permalink (copy-pasting an existing file and forgetting to
     change this) silently makes one publication's page overwrite another's,
     which happened once already in this repo - Jekyll's build output will
     warn about it ("... overwrites ...") if you get it wrong.
   - `excerpt`: the abstract. Shown collapsed (click "Abstract") in the
     publications list, and in full on the publication's own page.
3. Build the site (see below) and check the new entry shows up on
   `/publications/`, that its own page renders at the permalink you chose,
   and that it appears on the CV.
4. The CV PDF is regenerated automatically by a GitHub Action once this is
   pushed to `master` (see below) - no separate step needed.

## Updating the CV

- **Employment, education, honours**: edit `_data/cv.yml` directly.
- **Publications**: add/edit a file in `_publications/` as above - nothing
  else to touch.
- **Teaching**: add a file to `_teaching/` (a full course, gets its own
  page) or `_teaching_misc/` (a one-off, no dedicated page - see existing
  files for the fields each expects).
- **Organised events**: add a file to `_events/`.

All of the above feed both the on-site CV (`/cv/`) and the CV PDF - there is
nothing to duplicate or keep in sync by hand. The actual CV markup lives in
`_includes/cv-content.html`, shared between `_pages/cv.md` (on-site) and
`_pages/cv-print.md` (the PDF source, see next section) - if you need to
change the CV's layout or add a new section, that's the one file to edit.

### The CV PDF

`files/giacchetto_cv_en.pdf` (linked from the on-site CV's "Download the CV
as a PDF" button) is generated, not hand-maintained. It's produced by
`scripts/generate_cv_pdf.py`, which prints `/cv/print/` (a bare, nav-less
version of the CV built from the same `cv-content.html`) to PDF with
headless Chromium via Playwright.

A GitHub Actions workflow (`.github/workflows/cv-pdf.yml`) regenerates and
commits this PDF automatically whenever anything it depends on changes
(`_data/cv.yml`, `_publications/`, `_teaching*/`, `_events/`, the CV
templates) and lands on `master` - so in normal use you never need to run
this yourself. To regenerate it locally (e.g. to check a change before
pushing):

```bash
bundle exec jekyll build          # or the local-dev build command below
pip install playwright && playwright install chromium
python3 scripts/generate_cv_pdf.py
```

This overwrites `files/giacchetto_cv_en.pdf` in place. Sanity-check the
result before committing: open it and confirm the page count/layout look
right, and that links are clickable (they should point at real
`https://agiacche.github.io/...` URLs, not `localhost` - `_layouts/cv-print.html`
sets a `<base>` tag from `site.url` to make that work regardless of where
the PDF is generated from).

## Local development

This repo's `Gemfile` (via the `github-pages` gem) is what CI and a normal
local setup use - see `README.md` for the standard `bundle install` /
`bundle exec jekyll serve` instructions.

If you don't have network access to rubygems.org (e.g. in a restricted
sandbox) but do have Jekyll available some other way (e.g. via `apt`), a
`_config_dev.yml` override is included for exactly that case:

```bash
JEKYLL_NO_BUNDLER_REQUIRE=true jekyll build \
  --config _config.yml,_config_dev.yml --destination _site_test
```

This does two things on top of the normal config: it trims the plugin list
to whatever's actually available outside `bundler`, and it clears `url` so
that internal links/assets resolve relative to whatever host is serving the
build rather than to the real production domain - without this, a local
preview silently loads the *live* production CSS/JS instead of your local
changes, which is confusing. `_config_dev.yml` is never used by the real
production build (GitHub Pages only ever sees `_config.yml`), and
`_site_test/` is git-ignored.
