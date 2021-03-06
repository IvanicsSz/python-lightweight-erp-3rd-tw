# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table


def print_table(table, title_list=""):
    """print lists in a defined way"""
    max_str = 0
    table.insert(0, title_list)
    max_width_per_column = [max(y) for y in [[len(x[i]) for x in table] for i in range(len(table[0]))]]
    for i in max_width_per_column:
        max_str += i
    print("/{0:->{1}}".format("", max_str+len(title_list)-1), end="\\\n")
    for k, v in enumerate(table):
        for i, x in enumerate(v):
            if i < len(v)-1:
                print("|{0:^{1}}".format(x, max_width_per_column[i]), end="")
            if i == len(v)-1:
                print("|{0:^{1}}".format(x, max_width_per_column[i]), end="|\n")
        if k < len(table)-1:
            for j, y in enumerate(v):
                if j < len(v)-1:
                    print("|{0:-^{1}}".format("", max_width_per_column[j]), end="")
                if j == len(v)-1:
                    print("|{0:-^{1}}".format("", max_width_per_column[j]), end="|\n")
    print("\\{0:->{1}}".format("", max_str+len(title_list)-1), end="/\n")
    table.pop(0)
# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result


def print_result(result, label):
    """print functions results"""
    print(label)
    if type(result) is str:
        print(result)

    if type(result) is list:
        for i in result:
            print(i, sep=", ")

    if type(result) is dict:
        for key in result:
            print("{0}: {1}".format(key, result[key]))


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")


def print_menu(title, list_options, exit_message):
    """print menus with numbers in it"""
    print("{0}:".format(title))
    for i, v in enumerate(list_options, 1):
        print("({0}) {1}".format(i, v))
    print("(0) {0}".format(exit_message))


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title=""):
    """get input from the user"""
    print("{0}:".format(title))
    inputs = [input(i) for i in list_labels]
    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """print actual error messages"""
    print("Error: {0}".format(message))
