import pandas as pd
import numpy as np

"""Course CST8333_Assignment2
         Author :Simon Ao
         Student number:040983402"""

"""Class RecordData is a persistence layer, and only interact with csv file and business layer"""
class RecordData():

    """load records from csv file """
def load_100_records():

    """vaccination-coverage-byVaccineType.csv dataset file contains 10 columns
     the method will show 100 records form the provide dataset,then create a new array"""
column_list = ["prename", "prfname", "week_end", "product_name", "numtotal_atleast1dose", "numtotal_partially",
               "numtotal_fully", "prop_atleast1dose", "prop_partially", "prop_fully"]

"""Load the dataset from local drive, and use pandas to read csv file.
To have exception handling, this is to check whether the file exists or it has the correct name"""
try:
    dfread = pd.read_csv('vaccination-coverage-byVaccineType.csv ')
except FileNotFoundError:
    print('The file name invalid or file does not exist')

first_100_records = dfread.head(100)

filter_first_100_records = first_100_records[column_list]

array_read = np.array(filter_first_100_records)

"""print array_read """


def readloop():
    for i in array_read:
        if i <= 100:
            continue
        print(i)
    else:
        print("The above is Assignment 2 by Simon Ao")
