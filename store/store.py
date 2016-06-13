# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID",
                  "Title",
                  "Manufacturer",
                  "Price",
                  "Copies in stock"]

    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    print("hello add\n\n\n\n")

    # your code

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    print("hello remove\n\n\n\n")
    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    print("hello update\n\n\n\n")
    # your code

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    print("hello get counts by manufacturer\n\n\n\n")
    # your code

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    print("hello get average by manufacturer\n\n\n\n")
    # your code

    pass


def choose():
    table = data_manager.get_table_from_file("store/games.csv")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        remove(table, "placeholder")
    elif option == "4":
        update(table, "placeholder")
    elif option == "5":
        get_counts_by_manufacturers(table)
    elif option == "6":
        get_average_by_manufacturer(table, "placeholder")
    elif option == "0":
        return "stop"
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Show table",
               "Add record to table",
               "Remove record from table",
               "Update a record in table",
               "Number of game types by manufacturer",
               "Number of games in stock by a given manufacturer"]

    ui.print_menu("Store Manager menu", options, "Main menu")


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
def start_module():
    while True:
        handle_menu()
        try:
            choice = choose()
        except KeyError as err:
            ui.print_error_message(err)
        else:
            if choice == "stop":
                break
