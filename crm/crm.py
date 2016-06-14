# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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

#table = data_manager.get_table_from_file('/home/eszter/codecool/6_TW_week/python-lightweight-erp-3rd-tw/crm/customers.csv')

# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
def handle_menu():
    options = ["Show table",
                "Add a new record",
                "Remove a record",
                "Update records",
                "ID of the customer with the longest name",
                "E-mail subscriptions"]

    ui.print_menu("Customer Relationship Management [menu] \n", options, "Exit program \n")

def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "\n")
    table = data_manager.get_table_from_file('crm/customers.csv')

    option = inputs[0]
    if option == "1" or option == "3" or option == "4":
        show_table(table)
        if option == "3":
            id_ = ""
            while id_ not in [item[0] for item in table]:
                if id_ != "":
                    ui.print_error_message("ID given does not exist")
                id_ = ui.get_inputs(["Enter your ID: "], "")[0]
            remove(table, id_)
        elif option == "4":
            id_ = ""
            while id_ not in [item[0] for item in table]:
                if id_ != "":
                    ui.print_error_message("ID given does not exist")
                id_ = ui.get_inputs(["Enter your ID: "], "")[0]
            update(table, id_)
    elif option == "2":
        add(table)
    elif option == "5":
        get_longest_name_id(table)
    elif option == "6":
        get_subscribed_emails(table)
    elif option == "0":
        return "main"
    else:
        raise KeyError("There is no such option.")



def start_module():
    while True:
        handle_menu()
        try:
            if choose() == "main":
                break
        except KeyError as err:
            ui.print_error_message(err)


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):

    title_list = ["id", "Name", "E-mail address", "Subscription"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists


def add(table):
    title_list = ['id', 'name', 'e-mail', 'subscription']
    ui.print_table(table, title_list)

    new_record = ui.get_inputs(["Enter your name: ", "Enter your e-mail address: ", "Subscription (0/1 = no/yes): "], "Add a new record to the table")
    table = common.adding(table, new_record)

    # new_id = common.generate_random(table)
    # new_record.insert(0, new_id)
    # table.append(new_record)

    data_manager.write_table_to_file("crm/customers.csv", table)
    ui.print_table(table, title_list)

# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    # for item in table:
    #     if item[0] == id_:
    #         table.remove(item)

    common.removing(table, id_)
    data_manager.write_table_to_file("crm/customers.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    new_record = ui.get_inputs(["Enter your name: ", "Enter your e-mail address: ", "Subscription (0/1 = no/yes): "], "Update an existing record in the table")
    record = next(item for item in table if item[0] == id_)
    table[table.index(record)][1:] = new_record

    data_manager.write_table_to_file("crm/customers.csv", table)

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):
    name_max = max([len(item[1]) for item in table])
    list_names = [item[1] for item in table if len(item[1]) == name_max]
    list_sort = common.sorting(list_names)

    label = "What is the id of the customer with the longest name?"
    ui.print_result([item[0] for item in table if item[1] == list_sort[0]][0], label)
    return [item[0] for item in table if item[1] == list_sort[0]][0]


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    emails = [item for item in table if item[3] == '1']
    subscribed = [[item[2], item[1]] for item in emails]
    result = [';'.join([item[0], item[1]]) for item in subscribed]

    label = "Which customers have subscribed to the newsletter? \n"
    ui.print_result(result, label)
    return result
