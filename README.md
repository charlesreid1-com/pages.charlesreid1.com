# pages.charlesreid1.com

This is a simple single-page static landing page for 
the subdomain `pages.charlesreid1.com`.

The pages subdomain consists of repositories 
with a pages webhook - that is, a webhook 
that will deploy the `gh-pages` branch
of that repository as a page at

```
pages.charlesreid1.com/repo-name
```

This utilizes a webhook listener (see [b-captain-hook](https://git.charlesreid1.com/bots/b-captain-hook))
to listen for commits to particular repositories.
While not as streamlined as Github Pages 
(i.e., you still have to manually add a 
webhook to each repo you want to build a site for),
it provides a convenient, self-hosted alternative
to Github Pages.

This page uses a single-page Pelican theme to generate static content. 

Below, we cover:

* Generic Pelican Information
* Pages Subdomain Information
    * Setting up the webhook
    * Deploying the pages
    * Docker container with python web server
    * Reverse proxy with nginx

# Generic Pelican Information

## Required Software

To install Pelican:

```
pip install Markdown
pip install pelican
```

## Make Site

To make the Pelican site:

```
pelican content
cd output/
python -m http.server 8080
```

then visit `localhost:8080` in your browser.

## Modify Content

The single-site template utilizes variables defined in `pelicanconf.py` 
to customize the page content, so there is no content to edit in `content/`.

## Set Up Push to Github Pages

Start by cloning a copy of the repo at output (a repo within a repo):

```
git clone https://git.charlesreid1.com/charlesreid1/hooks.charlesreid1.com output/
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

