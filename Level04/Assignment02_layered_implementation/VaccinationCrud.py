import pandas as pd
import numpy as np
import VaccinationData as db

"""Course CST8333_Assignment2
         Author :Simon Ao
         Student number:040983402"""


class CrudRecord():
    """
      This is a business lay, and it is interact with persistence layer ( VaccinationData) and
      Presentation layer (VaccinationView)
      It will read data from VaccinationData, and create CRUD methods for Presentation layer
      """

    def display_records(self):
        """The display_records(self) method is to display/ print 100 records as a array data structure
        Data is loaded from VaccinationData class"""

        db.load_100_records
        print(db.array_read)

    def delete_record(self):
        """The delete_record(self) method is to select a specific record in the simple data structure,
        then delete it, after delete is done,
        write the updated array to a different csv file:'D:\ResearchLanguage\Assignment2.csv'"""

        delete_row = int(input("Select the row number to delete"))
        user_delete_array = np.delete(db.array_read, delete_row - 1, 0)
        print(user_delete_array)
        delete_dataframe = pd.DataFrame(user_delete_array)
        delete_dataframe.to_csv('D:\ResearchLanguage\Assignment2.csv', index=False, header=True)
        print("\n")

    def insert_record(self):
        """insert_record(self) method id create a new row, add it to first row of the simple data structure
        whit prename, prfname, week_end, product_name, numtotal_atleast1dose, numtotal_partially,
                numtotal_fully, prop_atleast1dose, prop_partially, prop_fully.
                It export a new record to another csv file:'D:\ResearchLanguage\Assignment2.csv' """

        input_prename = input("input a prename: ")
        input_prfname = input("input a prfname: ")
        input_week_end = input("input a week_end ")
        input_product_name = input("input a product_name: ")
        input_numtotal_atleast1dose = input("input a numtotal_atleast1dose: ")
        input_numtotal_partially = input("input a numtotal_partially: ")
        input_numtotal_fully = input("input a numtotal_fully: ")
        input_prop_atleast1dose = input("input a prop_atleast1dose: ")
        input_prop_partially = input("input a prop_partially: ")
        input_prop_fully = input("input a prop_fully: ")

        new_record = np.array(
            [input_prename, input_prfname, input_week_end, input_product_name, input_numtotal_atleast1dose,
             input_numtotal_partially, input_numtotal_fully, input_prop_atleast1dose, input_prop_partially,
             input_prop_fully])
        new_array = np.insert(db.array_read, 0, values=new_record, axis=0)
        print(new_array)
        create_dataframe = pd.DataFrame(new_array)
        create_dataframe.to_csv('D:\ResearchLanguage\Assignment2.csv', index=False, header=True)
        print("\n")

    def edit_record(self):
        """The edit_record(self) method has two function: read a selected record from the array,
        then user could decide if need to edit the record,
        after update the selected record whit prename, prfname, week_end, product_name,
         numtotal_atleast1dose, numtotal_partially,
                    numtotal_fully, prop_atleast1dose, prop_partially, prop_fully.
        the udpated array will export as csv file to 'D:\ResearchLanguage\Assignment2.csv'"""

        row_number = int(input("please input a row number less than 100: "))
        print(db.array_read[row_number].tolist())
        edit = input("Enter y to edit the  record or Enter q to go back to the homepage" + '\n')
        if edit == "q":
            pass
        if edit == "y":
            prename = input("reset prename: ")
            prfname = input("reset prfname: ")
            week_end = input("reset week_end: ")
            product_name = input("reset product_name: ")
            numtotal_atleast1dose = input("reset numtotal_atleast1dose: ")

            numtotal_partially = input("reset numtotal_partially: ")
            numtotal_fully = input("reset  numtotal_fully: ")
            prop_atleast1dose = input("reset prop_atleast1dose: ")
            prop_partially = input("reset prop_partially")
            prop_fully = input("reset prop_fully: ")

            db.array_read[row_number][0] = prename
            db.array_read[row_number][1] = prfname
            db.array_read[row_number][2] = week_end
            db.array_read[row_number][3] = product_name
            db.array_read[row_number][4] = numtotal_atleast1dose

            db.array_read[row_number][5] = numtotal_partially
            db.array_read[row_number][6] = numtotal_fully
            db.array_read[row_number][7] = prop_atleast1dose
            db.array_read[row_number][8] = prop_partially
            db.array_read[row_number][9] = prop_fully

            print(db.array_read[row_number].tolist())

            edit_dataframe = pd.DataFrame(db.array_read)
            edit_dataframe.to_csv('D:\ResearchLanguage\Assignment2.csv', index=False, header=True)
