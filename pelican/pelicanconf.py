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

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "pages.charlesreid1.com"
SITE_DESCRIPTION = "a subdomain for charlesreid1 pages"
GITEA_URL = "https://git.charlesreid1.com/charlesreid1/pages.charlesreid1.com"

# ---

# include <p> tags in the description

ABOUT_TITLE = "about pages.charlesreid1.com"

ABOUT_DESCRIPTION = """
<p>
<a href="https://git.charlesreid1.com/bots">bots on git.charlesreid1.com</a>
</p>

<p>&nbsp;</p>

<p><b>What is a bot?</b></p>

<p>Broadly, a bot is an autonomous entity that executes a program.<br />
The bots on this site are principally Twitter bot flocks.<br />
Also see <a href="https://twitter.com/horse_ebooks">@horse_ebooks</a>.</p>

<p>&nbsp;</p>

<p><b>What is a bot flock?</b></p>

<p>A bot flock is a group of Twitter bots that perform a related task,
access related data, or otherwise share some structure.<br />
See below for examples of Twitter bot flocks.</p>

<p>&nbsp;</p>

<p><b>Where can I find the bots?</b></p>

<p>Each bot has a home page on bots.charlesreid1.com; see below for links.</p>
"""


# ---


pages = {
    'rainbow-mind-machine' :    'https://pages.charlesreid1.com/rainbow-mind-machine',
    'apollo' :                  'https://pages.charlesreid1.com/apollo',
    'ginsberg' :                'https://pages.charlesreid1.com/ginsberg',
    'milton' :                  'https://pages.charlesreid1.com/milton',
    'tripos-bot' :              'https://pages.charlesreid1.com/tripos-bot'
}

LINKS_TITLE = "bot links"

LINKS_DESCRIPTION = """
'pages.charlesreid1.com' : '<i class="fa fa-file-o fa-fw"></i>',
"""


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
