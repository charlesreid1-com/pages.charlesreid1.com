#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import markdown

AUTHOR = u'charlesreid1'
SITENAME = u'charlesreid1 pages'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

# --------------8<---------------------

THEME = 'scurvy-knave-theme'

# Pelican is designed for files => pages.
# Use variables (below) to set pieces of pages.

# pages use twitter blue
INTROCOLOR  = "#fff"
ACOLOR      = "#00aced"
AHOVERCOLOR = "#0084b4"
BRIGHTCOLOR = "#1dcaff"
TEMPLATE_PAGES = {
    'custom.css' : 'custom.css'
}

INTROBKG='theme/img/intro-bg-foyer.jpg'
LINKSBKG='theme/img/links-bg-books.jpg'

# img/ should be in content/
# available at <url>/img
STATIC_PATHS = ['img']

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "pages.charlesreid1.com"
SITE_DESCRIPTION = "a subdomain for charlesreid1 pages"
GITEA_URL = "https://git.charlesreid1.com/charlesreid1/pages.charlesreid1.com"

# ---

about_md = markdown.Markdown(extensions=['extra','codehilite'],
                             output_format='html4')

ABOUT_SHORT = "About"

ABOUT_TITLE = "about pages.charlesreid1.com"

ABOUT_TEXT = """

pages.charlesreid1.com is a static site-hosting deployment solution provided by
[git.charlesreid1.com](https://git.charlesreid1.com).

<br />

**What is a static site?**

A static site is just a pile of static HTML, Javascript, CSS, and other files
that can be sent over to the host, and the host can render everything on their end.
(Compare with a dynamic site, which uses a language like PHP that requires the 
server to do the computations.)

<br />

**What does pages.charlesreid1.com provide?**

This provides a subdomain for hosting static sites associated with the repositories in 
[git.charlesreid1.com](https://git.charlesreid1.com).
</p>

It is a private, self-hosted solution that offers much of the same thing as what 
[Github Pages](https://pages.github.com)
(or simple [Heroku](https://heroku.com/) projects) offer.

<br />

**How is it hosted?**

This uses nginx, a fast, reliable, and easily-configurable web server.
The server with the static content is reverse-proxied by the frontend
server, which establishes secure connections and owns all of the 
SSL certificates.

<br />

**Who is this for?**

Pages can only be created/modified by users of <a href="https://git.charlesreid1.com">git.charlesreid1.com</a>
(i.e., me). They can be viewed by anyone (i.e., you).
"""

ABOUT_DESCRIPTION = about_md.convert(ABOUT_TEXT)


# ---


def make_pages():
    descr = ""

    pages = {
            'how-do-i-pelican' :        'https://pages.charlesreid1.com/how-do-i-pelican',
            'how-do-i-pandoc' :         'https://pages.charlesreid1.com/how-do-i-pandoc',
            'dont-sudo-pip' :           'https://pages.charlesreid1.com/dont-sudo-pip',

            'git-commit-ectomy' :       'https://pages.charlesreid1.com/git-commit-ectomy',

            'rainbow-mind-machine' :        'https://pages.charlesreid1.com/b-rainbow-mind-machine',
            'russian-rainbow-mind-machine': 'https://pages.charlesreid1.com/russian-rainbow-mind-machine',

            'b-apollo' :                'https://pages.charlesreid1.com/b-apollo',
            'b-ginsberg' :              'https://pages.charlesreid1.com/b-ginsberg',
            'b-milton' :                'https://pages.charlesreid1.com/b-milton',
            'b-captain-hook' :          'https://pages.charlesreid1.com/b-captain-hook',

            'pod-charlesreid1' :        'https://pages.charlesreid1.com/pod-charlesreid1',
            'pod-bots' :                'https://pages.charlesreid1.com/pod-bots',

            'd-gitea' :                 'https://pages.charlesreid1.com/d-gitea',
            'd-mediawiki' :             'https://pages.charlesreid1.com/d-mediawiki',
            'd-mysql' :                 'https://pages.charlesreid1.com/d-mysql',
            'd-nginx-charlesreid1' :    'https://pages.charlesreid1.com/d-nginx-charlesreid1',
            'd-nginx-subdomains' :      'https://pages.charlesreid1.com/d-nginx-subdomains',
            'd-phpmyadmin' :            'https://pages.charlesreid1.com/d-phpmyadmin',
            'd-python-files' :          'https://pages.charlesreid1.com/d-python-files',
            'd-python-helium' :         'https://pages.charlesreid1.com/d-python-helium',
    }

    descr += "<h3>charlesreid1 pages</h3>"
    fa_pages = '<i class="fa fa-globe fa-fw fa-2x"></i>'
    for page in pages.keys():
        url = pages[page]

        descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(url)
        descr += "%s %s"%(fa_pages, page)
        descr += "</a></p>\n"

    descr += "\n"

    return descr



LINKS_TITLE = "charlesreid1 pages"

LINKS_DESCRIPTION = make_pages()


# ---


CONTACT_TITLE = "Contact charlesreid1"

CONTACT_DESCRIPTION = """<p>Get in touch!</p>
<p><a href="mailto:charles@charlesreid1.com">charles (at) charlesreid1.com</a></p>
"""


# --------------8<---------------------

DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False
