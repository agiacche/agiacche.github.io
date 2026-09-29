source 'https://rubygems.org'

group :jekyll_plugins do
  gem 'jekyll'
  gem 'jekyll-feed'
  gem 'jekyll-sitemap'
  gem 'jekyll-redirect-from'
  gem 'jemoji'
  gem 'jekyll-gist'      # used by _config.yml's `plugins:` list; was pulled in
  gem 'jekyll-paginate'  # transitively via github-pages below - listed here now that it's gone
  gem 'webrick', '~> 1.8'
end

# 'github-pages' pins this whole tree to the exact ancient gem versions
# GitHub's Pages servers run (jekyll 3.10, kramdown 1.x-era plugins, etc.),
# so local `bundle install` matches production byte-for-byte. On Apple
# Silicon that chain drags in old C extensions (posix-spawn, yajl-ruby,
# rdiscount) that were never built for arm64-darwin and don't compile
# against a modern Ruby's C headers either - a well-known, essentially
# unfixable-locally incompatibility, not something wrong with this repo.
# Commented out rather than deleted: GitHub Pages' own build servers
# build the live site independently of this Gemfile.lock either way, so
# this only affects local preview, not what deploys. Uncomment it if you
# ever need to test against the exact GH Pages toolchain from an
# Intel Mac, Linux box, or under Rosetta.
# gem 'github-pages'
gem 'connection_pool', '2.5.0'
