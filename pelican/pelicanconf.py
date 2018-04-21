#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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

INTROBKG='theme/img/intro-bg-mist.jpg'
LINKSBKG='theme/img/links-bg-streetlamp.jpg'


# img/ should be in content/
# available at <url>/img
STATIC_PATHS = ['img']

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "pages.charlesreid1.com"
SITE_DESCRIPTION = "a subdomain for charlesreid1 pages"
GITEA_URL = "https://git.charlesreid1.com/charlesreid1/pages.charlesreid1.com"

# ---

# include <p> tags in the description

ABOUT_SHORT = "About"

ABOUT_TITLE = "about pages.charlesreid1.com"

ABOUT_DESCRIPTION = """
<p>
pages.charlesreid1.com is a static site-hosting deployment solution provided by
<a href="https://git.charlesreid1.com/">git.charlesreid1.com</a>.
</p>

<p>&nbsp;</p>

<p><b>What is a static site?</b></p>

<p>A static site is just a pile of static HTML, Javascript, CSS, and other files
that can be sent over to the host, and the host can render everything on their end.
(Compare with a dynamic site, which uses a language like PHP that requires the 
server to do the computations.)
</p>

<p><b>What does pages.charlesreid1.com provide?</b></p>

<p>This provides a subdomain for hosting static sites associated with the repositories in 
<a href="https://git.charlesreid1.com">git.charlesreid1.com</a>.
</p>

<p>It is a private, self-hosted solution that offers much of the same thing as what 
<a href="https://pages.github.com/">Github Pages</a> 
(or simple <a href="https://heroku.com/">Heroku</a> projects) offer.
</p>

<p>&nbsp;</p>

<p><b>How is it hosted?</b></p>

<p>This uses nginx, a fast, reliable, and easily-configurable web server.
The server with the static content is reverse-proxied by the frontend
server, which establishes secure connections and owns all of the 
SSL certificates.
</p>

<p>&nbsp;</p>

<p><b>Who is this for?</b></p>

<p>Pages can only be created/modified by users of <a href="https://git.charlesreid1.com">git.charlesreid1.com</a>
(i.e., me). They can be viewed by anyone (i.e., you).
</p>

"""

# ---


def make_pages():
    descr = ""

    pages = {
        'rainbow-mind-machine' :    'https://pages.charlesreid1.com/rainbow-mind-machine',
        'apollo' :                  'https://pages.charlesreid1.com/apollo',
        'ginsberg' :                'https://pages.charlesreid1.com/ginsberg',
        'milton' :                  'https://pages.charlesreid1.com/milton',
        'tripos-bot' :              'https://pages.charlesreid1.com/tripos-bot'
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
