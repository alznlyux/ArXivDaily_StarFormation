# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = 'alzn'

# The repository to add this issue to
REPO_OWNER = 'alzn'
REPO_NAME = 'ArXivDaily_StarFormation'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/astro-ph/new'

# Keywords to search
KEYWORD_LIST = ["star formation", "molecular cloud", "interstellar medium", "cloud", "clump", "core", "filament", "atomic gas", "N-PDF", "bubble", "shell", "HI"]
# Keywords to exclude
KEYWORD_EX_LIST = ["galaxies", "galaxy clusters", "AGN", "black hole", "dark matter", "planet", "fast radio burst", "z~"]
