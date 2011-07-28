import os, imp

def get_config(path):
    conf_source = path
    conf = imp.load_source('conf', conf_source)
    conf.backup_root = os.path.realpath(os.path.expanduser(conf.backup_root))
    return conf

def cleanup(snapshots):
    for s in snapshots:
        s.delete()
    
