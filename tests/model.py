import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+'/..'))

import unittest
from datetime import date
from src.model import Snapshot


today = date.strftime(date.today(), '%Y%m%d')

class TestSnapshot(unittest.TestCase):

    def setUp(self):
        self.root_path = os.path.abspath(os.path.dirname(__file__)+'/..')
        self.target_path = self.root_path+'/testfiles'
        self.snapshot = Snapshot(self.target_path+'/'+today+'.tar.bz2')

    def test0_save(self):
        self.snapshot.add(self.root_path+'/config.example.py')
        self.snapshot.save()
        self.assertTrue(os.path.isfile(self.target_path+'/'+today+'.tar.bz2'))
        
    def test1_delete(self):
        self.snapshot.delete()
        self.assertFalse(os.path.exists(self.target_path+'/'+today+'.tar.bz2'))
        
    def tearDown(self):
        try:
            os.rmdir(self.target_path)
        except OSError:
            pass
        
if __name__ == '__main__':
    unittest.main()