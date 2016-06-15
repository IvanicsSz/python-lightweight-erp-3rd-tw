# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
from datetime import date
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#

def handle_menu():
    options = ["Tool database",
               "Add new tool",
               "Remove tool",
               "Update tool data",
               "Tool(s) within durability",
               "Durability time per manufacturer"]
    ui.print_menu("Tool manager", options, "Back to main menu")


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    table = data_manager.get_table_from_file("tool_manager/tools.csv")
    if option == "1" or option == "3" or option == "4":
        show_table(table)
        if option == "3":
            id_ = ""
            while id_ not in [line[0] for line in table] and id_ != "0":
                if id_ != "":
                    ui.print_error_message("ID given does not exist")
                id_ = ui.get_inputs(["ID to be removed or 0 to exit:"])[0]
            if id_ != 0:
                remove(table, id_)
        if option == "4":
            id_ = ""
            while id_ not in [line[0] for line in table] and id_ != "0":
                if id_ != "":
                    ui.print_error_message("ID given does not exist")
                id_ = ui.get_inputs(["ID to be updated or 0 to exit:"])[0]
            if id_ != 0:
                update(table, id_)
    elif option == "2":
        add(table)
    elif option == "5":
        get_available_tools(table)
    elif option == "6":
        get_average_durability_by_manufacturers(table)
    elif option == "0":
        return "stop"
    else:
        raise KeyError("There is no such option.")


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


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    ui.print_table(table, title_list)
    return table


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    list_labels = [["Enter name or 0 to exit:"], ["Enter manufacturer or 0 to exit:"],
                   ["Enter purchase date or 0 to exit:"], ["Enter durability or 0 to exit:"]]
    new_tool_data = []
    for entry in list_labels:
        new_tool_data.append(ui.get_inputs(entry)[0])
        if "0" in new_tool_data:
            break
    if "0" not in new_tool_data:
        table = common.adding(table, new_tool_data)
        data_manager.write_table_to_file("tool_manager/tools.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    table = common.removing(table, id_)
    data_manager.write_table_to_file("tool_manager/tools.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    for line in table:
        if id_ in line:
            line[1:] = ui.get_inputs(["Enter name:", "Enter manufacturer:", "Enter date of purchase:",
                                     "Enter durability:"])
    data_manager.write_table_to_file("tool_manager/tools.csv", table)
    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):
    for line in table:
        line[3] = int(line[3])
        line[4] = int(line[4])
    available_tools = []
    actual_year = date.today().year
    for line in table:
        if (actual_year - (int(line[3]) + int(line[4]))) < 0:
            available_tools.append(line)
    ui.print_result(available_tools, "Tools available:")
    return available_tools


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    for line in table:
            line[4] = int(line[4])
    manufacturers = set([line[2] for line in table])
    average_dur = {}
    for line in manufacturers:
        durability = [x[4] for x in table if x[2] == line]
        average_dur[line] = common.summing(durability) / len(durability)
    ui.print_result(average_dur, "Average durability per manufacturer:")
    return average_dur
