import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+'/..'))

import unittest
from datetime import date
from src.model import Snapshot

today = date.strftime(date.today(), '%Y%m%d')

class TestSnapshot(unittest.TestCase):

    def setUp(self):
        self.path = os.path.abspath(os.path.dirname(__file__)+'/../testfiles')
        self.snapshot = Snapshot(self.path+'/'+today+'.tar.bz2')

    def test_creates_tarball(self):
        self.snapshot.add(self.path+'/..')
        self.snapshot.save()
        self.assertTrue(os.path.isfile(self.path+'/'+today+'.tar.bz2'))
        
    def test_delete(self):
        self.snapshot.delete()
        self.assertFalse(os.path.isfile(self.path+'/'+today+'.tar.bz2'))
        
    def tearDown(self):
        try:
            os.rmdir(self.path)
        except OSError:
            pass
        
if __name__ == '__main__':
    unittest.main()