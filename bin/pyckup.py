#!/usr/bin/env python

import os, sys
sys.path.append(os.path.dirname(__file__)+'/..')


def main():
    from src import manager
    from src.model import Snapshot, SnapshotManager
    
    conf = manager.get_config(os.path.dirname(__file__)+'/../conf.py')
    backup_path = "%s/%s" % (conf.backup_root, conf.backup_name)
    
    s = Snapshot(backup_path)
    s.add(conf.sources)
    s.save()
    



if __name__ == '__main__':
    main()