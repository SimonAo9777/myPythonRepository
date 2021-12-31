from operator import itemgetter

from VaccinationData import RecordData
import numpy as np
import pandas as pd
import csv

"""Course CST8333_Assignment3
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
        with open('vaccination-coverage-byVaccineType.csv', 'r') as df:
            file = csv.reader(df)
            list = list(file)
            print(list)
        return list
    def load_1000_records(self,list):
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


    def generic(self):
        """The demonstration method of the common input type is not defined,but can be modified as needed."""
        input = input("Please enter a number")
        print(type(input))
        int(input)
        print(type(input))

    def test_out_format(self,firsttype,secondtype):
        """This method to test the two types of datatype"""
        validate = type(firsttype) !=type(secondtype)
        return validate