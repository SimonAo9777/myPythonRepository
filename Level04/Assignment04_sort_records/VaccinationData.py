import pandas as pd
import numpy as np
import sqlalchemy


"""Course CST8333_Assignment4
         Author :Simon Ao
         Student number:040983402"""

"""Class RecordData is a persistence layer, and only interact with csv file and business layer"""

class RecordData():
    """load records from csv file """


    def __init__(self):
        """Constructor of RecordData object """


    def load_1000_records(self):
        """vaccination-coverage-byVaccineType.csv dataset file contains 10 columns
             the method will show 1000 records form the provide dataset,then create a new array"""


        column_list = ["prename", "prfname", "week_end", "product_name", "numtotal_atleast1dose", "numtotal_partially",
                       "numtotal_fully", "prop_atleast1dose", "prop_partially", "prop_fully"]
        dfread = pd.read_csv('vaccination-coverage-byVaccineType.csv')
        first_1000_records = dfread.head(1000)
        filter_first_1000_records = first_1000_records[column_list]
        data_1000 = np.array(filter_first_1000_records)
        print(column_list)
        print(data_1000)
        return data_1000

    def load_all_records(self):
        """vaccination-coverage-byVaccineType.csv dataset file contains 10 columns
                 the method will show all records form the provide dataset,then create a new array"""

        column_list = ["prename", "prfname", "week_end", "product_name", "numtotal_atleast1dose", "numtotal_partially",
                       "numtotal_fully", "prop_atleast1dose", "prop_partially", "prop_fully"]
        dfread = pd.read_csv('vaccination-coverage-byVaccineType.csv')
        data_all_record = dfread.head(3080)
        filter_data_all = data_all_record[column_list]
        data_all = np.array(filter_data_all)
        print(column_list)
        print(data_all)
        return data_all

    def created_mySQL_connection(self):
        """Created MySQL connection,load all records with header from csv file to MySQL"""

        dfread = pd.read_csv('vaccination-coverage-byVaccineType.csv')

        engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:aodaxia2021@localhost')
        engine.execute("DROP DATABASE IF EXISTS vaccinationtypedatabase")  # drop existed database
        engine.execute("CREATE DATABASE vaccinationtypedatabase")  # create database
        engine.execute("USE vaccinationtypedatabase")  # select new database
        with engine.connect() as conn, conn.begin():
            dfread.to_sql('types', conn, if_exists='replace', index=True)


def load_100_records():
    """vaccination-coverage-byVaccineType.csv dataset file contains 10 columns
     the method will show 100 records form the provide dataset,then create a new array"""


column_list = ["prename", "prfname", "week_end", "product_name", "numtotal_atleast1dose", "numtotal_partially",
               "numtotal_fully", "prop_atleast1dose", "prop_partially", "prop_fully"]
try:
    dfread = pd.read_csv('vaccination-coverage-byVaccineType.csv ')
except FileNotFoundError:
    print('The file name invalid or file does not exist')

first_100_records = dfread.head(100)

filter_first_100_records = first_100_records[column_list]

array_read = np.array(filter_first_100_records)

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
        print("The above is Assignment 4 by Simon Ao")
