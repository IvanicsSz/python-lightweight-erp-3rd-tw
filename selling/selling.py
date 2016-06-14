# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
    options = ["Show selling table",
               "Add record to selling table",
               "Remove record from selling table",
               "Update record in selling table",
               "Items are sold between dates",
               "Id of the item that sold for the lowest price"
               ]
    ui.print_menu("Selling menu", options, "Back to Main Menu")


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    table = data_manager.get_table_from_file("selling/sellings.csv")
    global back_to_main
    if option == "1" or option == "3" or option == "4":
        show_table(table)
        if option == "3":
            id_ = ui.get_inputs(["Please select the record to delete: "])[0]
            remove(table, id_)
        if option == "4":
            id_ = ui.get_inputs(["Please select the record to update: "])[0]
            update(table, id_)
    elif option == "2":
        add(table)
    elif option == "5":
        get_lowest_price_item_id(table)
    elif option == "6":
        year = ui.get_inputs(["Please insert the month form",
                              "Please insert the day form",
                              "Please insert the year form",
                              "Please insert the month to",
                              "Please insert the day to",
                              "Please insert the year to"
                              ], "")[0]
        get_items_sold_between(table, int(month_from), int(day_from ), int(year_from), int(month_to), int(day_to), int(year_to))
    elif option == "0":
        back_to_main = 1
    else:
        raise KeyError("There is no such option.")



# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    ui.print_table(table, ["id", "title", "price", "month", "day", "year"])

#
# show_table(table)



# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    content = ui.get_inputs(["Please add title: ",
                             "Please add price: ",
                             "Please add month: ",
                             "Please add day: ",
                             "Please add year: "
                             ])
    table = common.adding(table, content)
    data_manager.write_table_to_file("selling/sellings.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    table = common.removing(table, id_)
    data_manager.write_table_to_file("selling/sellings.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    content = ui.get_inputs(["Please add new title: ",
                             "Please add new price: ",
                             "Please add new month: ",
                             "Please add new day: ",
                             "Please add new year: "
                             ])
    table = common.updating(table, id_, content)
    data_manager.write_table_to_file("selling/sellings.csv", table)
    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):
    lowest = [(i[2], i[0]) for i in table]
    lowest = common.sorting(lowest)
    return lowest[0][1]


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code

    pass
