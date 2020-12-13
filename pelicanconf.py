#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Geoff St. Pierre (serundeputy)'
SITENAME = 'serundeputy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
          ('{ about }', '/about'),
          ('{ contributions }', '/contributions'),
        )

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['/home/gff/code/personal/pelican-plugins']
PLUGINS = ['i18n_subsites',]
THEME = 'themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
STATIC_PATHS = {
    'images',
    'extra',
}
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
