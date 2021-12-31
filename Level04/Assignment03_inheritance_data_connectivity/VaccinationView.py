from self import self
from VaccinationCrud import CrudRecord

"""Course CST8333_Assignment3
         Author :Simon Ao
         Student number:040983402"""


class Launcher():
    """Launcher class is the presentation lay, interact with user and business layer (_CrudRecordClass_)
       The function is for user to be able to create, read, update, delete the simple data structure.
    """

    def __init__(self):
        """Construct the main class and set the parameter to self"""

    def startOperation(self):
        """
        The startOperation(self) methods iterate the user's input and call the appropriate operation
        It will print menu, and accept user's input
        """
        while True:  # Display action option
            print("1. Enter number 1 to reload the records: " + "\n" +
                  "2. Enter number 2 to select to view or edit a record: " + "\n" +
                  "3. Enter number 3 to create a new record: " + "\n" +
                  "4. Enter number 4 to delete a record: " + "\n" +
                  "5. Enter number 5 to reload 1000 records form list: " + "\n" +
                  "6. Enter q to exit " + "\n")
            i = input("Please choose one number: ")  # Options to select
            if i == '1':
                CrudRecord.display_records(self)
                print("Course CST8333_Assignment3" + "\n" +
                      "author :Simon Ao" + "\n" +
                      "student number:040983402")
                pass
            if i == '2':
                CrudRecord.edit_record(self)
                print("Course CST8333_Assignment3" + "\n" +
                      "author :Simon Ao" + "\n" +
                      "student number:040983402")
                pass
            if i == '3':
                CrudRecord.insert_record(self)
                print("Course CST8333_Assignment3" + "\n" +
                      "author :Simon Ao" + "\n" +
                      "student number:040983402")
                pass
            if i == '4':
                CrudRecord.delete_record(self)
                print("Course CST8333_Assignment3" + "\n" +
                      "author :Simon Ao" + "\n" +
                      "student number:040983402")
                pass
            if i == '5':
                CrudRecord.display_sortedlist(list)
                print("Course CST8333_Assignment3" + "\n" +
                      "author :Simon Ao" + "\n" +
                      "student number:040983402")
                pass
            if i == 'q':
                break
            else:
                print("please re-enter a number")


if __name__ == "__main__":
    """Execute program form here """
    Launcher()
    Launcher.startOperation(self)
print("StudentName: Simon Ao,StudentNumber:040983402")
