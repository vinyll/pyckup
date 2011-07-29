## SPECIFIC CONF ##

# Tuple of files and dirs to save
sources = ()

# Path to folder holding snapshots
backup_root = "~"



## MAIN CONF ##

from datetime import date

# file name of the snapshot. Relative to backup_root
backup_name = '%s.tar.bz2' % date.strftime(date.today(), '%Y%m%d')

# list of days to preserve copies from today
# @todo: use this to clean files
backup_days = [1, 2, 3, 7, 30]

## LOGGING ##

import logging

# File to store log
log_file = ''

# Minimal level to store log. see logging module warn levels
log_level = 1

# String format for logging rows
logging.BASIC_FORMAT = "%(levelname)s - Pyckup/%(name)s : %(message)s"
