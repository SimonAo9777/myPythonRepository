from operator import itemgetter

from VaccinationData import RecordData
import pandas as pd
import csv

"""Course CST8333_Assignment4
         Author :Simon Ao
         Student number:040983402"""


class ChildRecordData(RecordData):
    """This is subclass for data layer.
       This class inherited all methods from superclass ChildRecordData, and also override two methods
       sub class also can implement new methods"""

    def __init__(self, list):
        """constructor for ChildRecordData object.
                It overwrites superclass constructor with parameter list"""
        super().__init__()
        self.list = list

    def create_mySQL_connection(self):
        """Inherited method"""

    pass

    def load_all_records(self, list):
        """Inherited method,override to output of all records as list"""
        column_list = ["prename", "prfname", "week_end", "product_name", "numtotal_atleast1dose", "numtotal_partially",
                       "numtotal_fully", "prop_atleast1dose", "prop_partially", "prop_fully"]
        with open('vaccination-coverage-byVaccineType.csv', 'r') as dfred:
            file = csv.reader(dfred)
            list = list(file)
            print(list)
        return list





    def load_1000_records(self, list):
        """Inherited method,override to output of 1000 records as list"""
        column_list = ["prename", "prfname", "week_end", "product_name", "numtotal_atleast1dose", "numtotal_partially",
                       "numtotal_fully", "prop_atleast1dose", "prop_partially", "prop_fully"]
        dfred = pd.read_csv('vaccination-coverage-byVaccineType.csv')
        first_1000_records = dfred.head(1000)
        filter_first_1000_records = first_1000_records[column_list]
        lists_1000 = filter_first_1000_records
        lists_1000 = lists_1000.values.tolist()
        lists_1000 = sorted(lists_1000, key=itemgetter(2))
        lists_1000.insert(0, filter_first_1000_records.columns.tolist())
        for i in lists_1000:
            print(i)
        print(len(lists_1000))
        return list

    def sort_input_records(self, list):
        """Inheritance method, overridden to output all records as a list and allow two digits to be
        sorted at the same time, and finally the output list sorted by the total number of rows"""

        dfred = pd.read_csv('vaccination-coverage-byVaccineType.csv')
        list = dfred.values.tolist()
        i = int(input("Please enter a number: "))
        j = int(input("Please enter a number: "))
        if 0 < i <= 10:
            if 0 <= j <= 10:
                list_s = sorted(list, key=itemgetter(i, j))  # sort by key
                list_s.insert(0, dfred.columns.tolist())
                for i in list_s:
                    print(i)
                print(len(list_s))
            return list_s





def test_out_format(self, firsttype, secondtype):
    """This method to test the two types of datatype"""
    validate = type(firsttype) != type(secondtype)
    return validate
