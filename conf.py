import os
from datetime import date

# Path to folder holding snapshots
backup_root = "~/backup/mytest"

# Tuple of files and dirs to save
sources = (
    os.path.dirname(__file__),
    '~/worktimer/datas',
)

# file name of the snapshot. Relative to backup_root
backup_name = '%s.tar.bz2' % date.strftime(date.today(), '%Y%m%d')

