
## SPECIFIC CONF ##

import os

# Path to folder holding snapshots
backup_root = "~/backup/mytest"

# Tuple of files and dirs to save
sources = (
    os.path.dirname(__file__),
    '~/worktimer/datas',
)



## MAIN CONF ##

from datetime import date

# file name of the snapshot. Relative to backup_root
backup_name = '%s.tar.bz2' % date.strftime(date.today(), '%Y%m%d')



## LOGGING ##

import logging

# File to store log
log_file = ""

# Minimal level to store log. see logging module warn levels
log_level = logging.WARNING
