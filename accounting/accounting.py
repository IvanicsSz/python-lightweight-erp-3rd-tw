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
               "Add record to accounting table",
               "Remove record from accounting table",
               "Update record in accounting table",
               "Show the year of highest profit",
               "Show the average profit for the year"]

    ui.print_menu("Accounting menu", options, "Back to main menu")


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    table = data_manager.get_table_from_file("accounting/items.csv")
    global back_to_main
    if option == "1" or option == "3" or option == "4":
        show_table(table)
        if option == "3":
            id_ = ui.get_inputs(["Please select the record to delete: "], "")[0]
            remove(table, id_)
        if option == "4":
            id_ = ui.get_inputs(["Please select the record to update: "], "")[0]
            update(table, id_)
    elif option == "2":
        add(table)
    elif option == "5":
        which_year_max(table)
    elif option == "6":
        year = ui.get_inputs(["Please insert the year"], "")[0]
        avg_amount(table, int(year))
    elif option == "0":
        back_to_main = 1
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["Id",
                  "Month",
                  "Day",
                  "Year",
                  "Type",
                  "Amount (dollar)"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title = "Adding new record to accounting table"
    list_labels = ["Month",
                   "Day",
                   "Year",
                   "Type",
                   "Amount (dollar)"]
    record = ui.get_inputs(list_labels, title)
    record.insert(0, common.generate_random(table))
    table.append(record)
    data_manager.write_table_to_file("accounting/items.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    table.remove([x for x in table if x[0] == id_][0])
    data_manager.write_table_to_file("accounting/items.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    title = "Updating record in accounting table"
    list_labels = ["Month",
                   "Day",
                   "Year",
                   "Type",
                   "Amount (dollar)"]
    record = ui.get_inputs(list_labels, title)
    record.insert(0, id_)
    table[table.index([x for x in table if x[0] == id_][0])] = record
    data_manager.write_table_to_file("accounting/items.csv", table)
    return table


# special functions:
# ------------------
def sum_profit(table, year):
    res = 0
    for i in [[x[5], x[4]] for x in table if x[3] == str(year)]:
        if i[1] == "in":
            res += int(i[0])
        else:
            res -= int(i[0])
    return res


# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    profit_list = []
    for i in list(set(x[3] for x in table)):
        profit_list.append([sum_profit(table, i), i])
    result = [x[1] for x in profit_list if x[0] == max([x[0] for x in profit_list])][0]
    ui.print_result(result, "The year which had most in and outcome profit")
    return result


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    profit = sum_profit(table, year)
    result = profit / len([x for x in table if x[3] == str(year)])
    ui.print_result(str(result), "Average profit (per item) in the given year is")
    return result
