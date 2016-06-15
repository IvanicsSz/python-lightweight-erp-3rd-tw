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
back_to_main = 0

# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#


def start_module():
    global back_to_main
    while not back_to_main:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(err)
    back_to_main = 0


def handle_menu():
    options = ["Show accounting table",
               "Adding new record",
               "Removing record",
               "Updating record",
               "Show year of highest profit",
               "Show average profit for a year"]
    ui.print_menu("Accounting menu", options, "Back to main menu")


def choose():
    option = ui.get_inputs(["Please enter a number: "])[0]
    table = data_manager.get_table_from_file("accounting/items.csv")
    global back_to_main
    if option == "1" or option == "3" or option == "4":
        show_table(table)
        if option == "3":
            id_ = ui.get_inputs(["Please select the record to delete: "])[0]
            remove(table, id_)
        elif option == "4":
            id_ = ui.get_inputs(["Please select the record to update: "])[0]
            update(table, id_)
    elif option == "2":
        add(table)
    elif option == "5":
        ui.print_result(str(which_year_max(table)), "The year with most profit is: ")
    elif option == "6":
        year = ui.get_inputs(["Please insert the year: "])[0]
        ui.print_result(str(avg_amount(table, int(year))), "Average profit per item in given year: ")
    elif option == "0":
        back_to_main = 1
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    ui.print_table(table, ["Id", "Month", "Day", "Year", "Type", "Amount"])


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    table = common.adding(table, ui.get_inputs(["Month: ", "Day: ", "Year: ", "Type: ", "Amount (dollar): "]))
    data_manager.write_table_to_file("accounting/items.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    table = common.removing(table, id_)
    data_manager.write_table_to_file("accounting/items.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    table = common.updating(table, id_, ui.get_inputs(["Month: ", "Day: ", "Year: ", "Type: ", "Amount (dollar): "]))
    data_manager.write_table_to_file("accounting/items.csv", table)
    return table


# special functions:
# ------------------
def sum_profit(table, year):
    res = common.summing([int(x[5]) for x in table if x[3] == str(year) and x[4] == "in"])
    return res - common.summing([int(x[5]) for x in table if x[3] == str(year) and x[4] == "out"])


# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    profit_list = [[sum_profit(table, i), i] for i in list(set(x[3] for x in table))]
    result = [x[1] for x in profit_list if x[0] == max([x[0] for x in profit_list])][0]
    return int(result)


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    result = sum_profit(table, year) / len([x for x in table if x[3] == str(year)])
    return result
