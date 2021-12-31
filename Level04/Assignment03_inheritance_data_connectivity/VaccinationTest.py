import unittest
import pandas as pd
import numpy as np
from VaccinationData import RecordData
from childVaccinationData import ChildRecordData

"""Course CST8333_Assignment3
         Author :Simon Ao
         Student number:040983402"""

"""The unit test class,read CSV file 1000 records as data frame and print Array or list"""

class VaccinationTest(unittest.TestCase):

    def test_read_records(self):
        """Compare the super class data output with array and subclass data out put with lists"""
        dfread = pd.read_csv('vaccination-coverage-byVaccineType.csv')
        array = np.array(dfread)
        list = array.tolist()
        superclass = RecordData()
        subclass = ChildRecordData(list)

        test_out_format_result = subclass.test_out_format(subclass.load_1000_records(list), superclass.load_1000_records())

        self.assertTrue(test_out_format_result)


if __name__ == '__main__':
    # Execute test program form here
    unittest.main()
