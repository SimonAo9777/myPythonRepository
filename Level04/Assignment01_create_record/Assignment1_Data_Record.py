# Student name:Simon Ao
import pandas as pd
import numpy as np


def studentIfo():
    """Course CST8333_Assignment1
         Author :Simon Ao
         Student number:040983402
    """


print(studentIfo.__doc__)

""" vaccination-coverage-byVaccineType.csv dataset file contains 10 columns 
"""

column_number = ["prename", "prfname", "week_end", "product_name", "numtotal_atleast1dose", "numtotal_partially",
                 "numtotal_fully", "prop_atleast1dose", "prop_partially", "prop_fully"]

""" Load the dataset from local drive,  use pandas to read vaccination-coverage-byVaccineType.csv dataset file. 
Exception handling to check if file is exist or it has correct name.
"""

try:
    csv_dataframe_1 = pd.read_csv('D:\ResearchLanguage/vaccination-coverage-byVaccineType.csv')
except FileNotFoundError:
    print('The file name is incorrect or the file does not exist, please re-enter')

data_10_records = csv_dataframe_1.head(10)
print(data_10_records)

choose_data_10_records = data_10_records[column_number]
print(choose_data_10_records)

array1 = np.array(choose_data_10_records)
print(array1)


def data_records():
    """ The method is to promote the  first 10 records from the memory to the local drive D:
    """


try:
    choose_data_10_records.to_csv('D:\ResearchLanguage\Assignment1.csv', index=True, header=True)

except FileNotFoundError:
    print('If file path could not found, please check your file')


def display_data_records():
    """The method is to display all row"""

    print(choose_data_10_records.columns.values.tolist())
    print(array1)

    """How to do looping to print arraylist array1"""


for i in array1:
    print(i)
else:
    print("Simon Ao printed top 10 records!")
