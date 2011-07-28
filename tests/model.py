import os, sys
from datetime import date

sys.path.append(os.path.realpath(os.path.dirname(__file__)+'/../'))

import unittest
from src.model import Snapshot

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.path = os.path.abspath(os.path.dirname(__file__))+'/../testfiles'
        self.snapshot = Snapshot(self.path)

    def test_creates_tarball(self):
        str_date = date.strftime(date.today(), '%Y%m%d')
        self.snapshot.add(self.path)
        self.snapshot.save()
        print self.path
        self.assertTrue(os.path.isfile(self.path+'/'+str_date+'.tar.bz2'))

if __name__ == '__main__':
    unittest.main()