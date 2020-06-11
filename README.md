# pages.charlesreid1.com

This repo contains files for creating the static page at pages.charlesreid1.com.

This repo also serves static content from several other repositories, via submodules
in the `gh-pages` branch.

## TOC

* branches
* submodules in gh-pages branch
* pages.charlesreid1.com static site
* generic pelican information
* make site
* modify content
* set up push to github pages

## Branches

The `master` branch contains the files needed to generate pages.charlesreid1.com.

The `gh-pages` branch contains the generated pages.charlesreid1.com page, as well as
several git submodules that point to other `gh-pages` branches of other repositories.

## Submodules in gh-pages branch

Submodules make it easier to update the content of other repos.

Github Pages transparently serves up other repos' `gh-pages` branches.
This includes repos that have CNAME records created for them.

So a submodule that lives on the `gh-pages` branch at `project-name` and points to
the `gh-pages` branch of `org-name/project-name`, the `gh-pages` branch of `project-name`
will be served up via the following URL:

```
pages.charlesreid1.com/project-name
```

where `pages.charlesreid1.com` points to the `gh-pages` branch of this repo,
and `pages.charlesreid1.com/project-name` points to the `gh-pages` branch of the
`project-name` repo.

## pages.charlesreid1.com static site

This page uses a single-page Pelican theme to generate static content. 

The sections below cover how to generate the content of the static site
using Pelican.

## Generic Pelican Information

### Quick Start

Clone the repo to get started

```
git clone https://github.com/charlesreid1-com/pages.charlesreid1.com
cd pages.charlesreid1.com
```

### Required Software

To install Pelican:

```
pip install Markdown
pip install pelican
```

This uses the scurvy knave pelican theme. To install this theme,
see <https://github.com/charlesreid1/scurvy-knave-theme>.

## Make Site

To make the Pelican site, starting at the repository root:

```
cd pelican/
pelican content
cd output/
python -m http.server 8080
```

then visit `localhost:8080` in your browser.

## Modify Content

The single-site template utilizes variables defined in `pelicanconf.py` 
to customize the page content, so there is no content to edit in `content/`.

## Set Up Push to Github Pages

Start by cloning a copy of the repo at the `output/` directory in the `pelican` folder of the repo.
We will make a brand new branch called `gh-pages` that shares no history or commits
with any other branches (orphan branch):

```
git clone https://github.com/charlesreid1-com/pages.charlesreid1.com output/
cd output/
git checkout --orphan gh-pages
cd ../
```

Now make the content, which will put the resulting pages into `output/`,
and commit the new version of the site to the `gh-pages` branch:

```
pelican content
cd output/
git add -A .
git commit -a -m 'Add new version of site'
git push origin gh-pages
```

