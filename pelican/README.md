# pages.charlesreid1.com

pages.charlesreid1.com is a subdomain for hosting static site content,
similar to Github pages.

## Repository Layout

Source branch: `master`

Live/pages branch: `gh-pages`

This repository is hosted by the [`d-nginx-subdomain`](https://git.charlesreid1.com/docker/d-nginx-subdomain)
container and is serviced/utilized/updated 
by the captain hook webhook server, [`b-captain-hook`](https://git.charlesreid1.com/bots/b-captain-hook).

## Containerization

This repository contains the static content.

The containerized version is in [`d-nginx-subdomain`](https://git.charlesreid1.com/docker/d-nginx-subdomain).

The subdomains container is run on blackbeard using nginx
to host the static content and handle the different subdomains,
all reverse-proxied by krash on the frontend.

