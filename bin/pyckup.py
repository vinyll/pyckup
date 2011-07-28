#!/usr/bin/env python

import os, sys
sys.path.extend([
     os.path.realpath(os.path.dirname(__file__)+'/../packages'),
     os.path.realpath(os.path.dirname(__file__)+'/..')
])



import argparse, logging, imp
from src.model import Snapshot


def parse_args():
    parser = argparse.ArgumentParser(description='This is a PyMOTW sample program')
    parser.add_argument('--config-file', dest="config_file", type=file)
    return parser.parse_args()
    

def main(args):
    conf = imp.load_source('conf', args.config_file.name)
    logging.basicConfig(filename=conf.log_file, level=conf.log_level)
    logging.debug('** new Pyckup call **')
    logging.debug('Loading config from file %s' % args.config_file.name)
    conf.backup_root = os.path.realpath(os.path.expanduser(conf.backup_root))
    
    backup_path = "%s/%s" % (conf.backup_root, conf.backup_name)
    
    s = Snapshot(backup_path)
    s.add(conf.sources)
    s.save()
    


if __name__ == '__main__':
    main(parse_args())