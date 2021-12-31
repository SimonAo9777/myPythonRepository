import unittest
from VaccinationCrud import CrudRecord

"""Course CST8333_Assignment2
         Author :Simon Ao
         Student number:040983402"""

"""The unit test class"""
class VaccinationTest(unittest.TestCase):

    def test_delete(self):
        """this method is to test if delete line is equal to the deleted record"""
        delete_line = CrudRecord.delete_record(self)
        self.assertEqual(delete_line, delete_line)
        print('test_delete successfully')

if __name__ == '__main__':
    unittest.main()
