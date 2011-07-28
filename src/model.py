import os, tarfile
import logging

class Snapshot(object):
    
    files = []
    compression = 'bz2' # empty, 'gz' or 'bz2'
    
    def __init__(self, filepath):
        """
        filepath is the snapshot filepath path
        """
        self.filepath = os.path.realpath(os.path.expanduser(filepath))
    
    def __repr__(self):
        return self.filepath
    
    def add(self, paths):
        """
        Add a filepath or folder to the backup
        path is a string or tuple represeting the full path of the file/folder
        """
        if isinstance(paths, str):
            paths = [paths]
        
        for p in paths:
            p = os.path.realpath(os.path.expanduser(p))
            if not os.path.exists(p):
                logging.warning('Path "%s" cannot be added to %s', p, self)
            else:
                self.files.append(p)
        
        logging.debug('added following files/dirs to %s : %s' % (self, ', '.join(self.files)))
    
    @property
    def path(self):
        return self.filepath
    
    def save(self):
        dir = os.path.dirname(self.filepath)
        if not os.path.isdir(dir):
            os.makedirs(dir)
        out = tarfile.TarFile.open(self.filepath, 'w:'+self.compression)

        for file in self.files:
            out.add(file, arcname=os.path.basename(file))
        out.close()
        
        logging.debug('saved %s' % self)
    
    def is_snapshot(self):
        return tarfile.is_tarfile(self.path)
    
    def delete(self):
        os.remove(self.filepath)
        logging.debug('deleted %s' % self)
    

class SnapshotManager(object):
    def __init__(self, path):
        self.path = os.path.realpath(os.path.expanduser(path))
    
    def all(self):
        """
        Retrieves all files detected as snapshop in specified directory
        """
        snapshots = []
        for p in os.listdir(self.path):
            s = Snapshot(os.path.join(self.path, p))
            if s.is_snapshot:
                snapshots.append(s)
        return snapshots
    