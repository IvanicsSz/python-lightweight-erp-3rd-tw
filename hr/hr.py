# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def handle_menu():
    options = ["Employee database",
               "Add new employee",
               "Remove employee",
               "Update employee data",
               "Oldest employee",
               "Employee with average age"]
    ui.print_menu("Human resources manager", options, "Back to main menu")


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    table = data_manager.get_table_from_file("hr/persons.csv")
    if option == "1" or option == "3" or option == "4":
        show_table(table)
        if option == "3":
            id_ = ui.get_inputs(["ID to be removed:"])
            remove(table, id_[0])
        if option == "4":
            id_ = ui.get_inputs(["ID to be updated:"])
            update(table, id_[0])
    elif option == "2":
        add(table)
    elif option == "5":
        get_oldest_person(table)
    elif option == "6":
        get_persons_closest_to_average(table)
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
    title_list = ["ID", "Name", "Date of birth"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    list_labels = ["Enter name:", "Enter date of birth:"]
    new_id_ = common.generate_random(table)
    new_employee_data = ui.get_inputs(list_labels)
    new_employee_data.insert(0, new_id_)
    table.append(new_employee_data)
    data_manager.write_table_to_file("hr/persons.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    for line in table:
        if id_ in line:
            table.remove(line)
    data_manager.write_table_to_file("hr/persons.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    for line in table:
        if id_ in line:
            line[1:] = ui.get_inputs(["Enter name:", "Enter date of birth:"])
    data_manager.write_table_to_file("hr/persons.csv", table)
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    max_year = min([data[2] for data in table])
    oldest_employee = []
    for line in table:
        if max_year in line:
            oldest_employee.append(line[1])
    ui.print_result(oldest_employee, "Oldest employee(s):")
    return oldest_employee


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    average_year = float(common.summing([int(line[2]) for line in table]) // len(table))
    min_diff = min([abs(int(line[2]) - average_year) for line in table])
    closest_average = [line[1] for line in table if abs(int(line[2]) - average_year) == min_diff]
    ui.print_result(closest_average, "Employee closest to average age:")
    return closest_average
