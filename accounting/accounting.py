# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


# importing everything you need
import os
import random
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()
# make table global variable

# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#


def start_module():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(err)


def handle_menu():
    options = ["Show accounting table",
               "Add record to accounting table",
               "Remove record from accounting table",
               "Update record in accounting table",
               "Show the year of highest profit",
               "Show the average profit for the year"]

    ui.print_menu("Accounting menu", options, "Back to main menu")


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    table = data_manager.get_table_from_file("items.csv")
    option = inputs[0]
    if option == "1" or option == "3" or option == "4":
        show_table(table)
        if option == "3":
            id_ = input("Please select the record to remove")
            remove(table, id_)
        if option == "4":
            id_ = input("Please select the record to update")
            update(table, id_)
    elif option == "2":
        add(table)
    elif option == "5":
        which_year_max(table)
    elif option == "6":
        year = input("Please enter a year")
        avg_amount(table)
    elif option == "0":
        pass
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    pass
