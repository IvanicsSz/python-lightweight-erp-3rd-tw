# implement commonly used functions here
import string
import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):
    generated = ""
    while(generated == "" or generated in [x[0] for x in table]):
        abc = [string.digits, string.ascii_uppercase, string.ascii_lowercase]
        for i in range(-5, 6, 2):
            generated += random.choice(abc[abs(i)//2])
        generated += "#&"
    return generated


def sorting(list_sort, index=""):
    """sorting an unsorted list  """

    for i in range(len(list_sort)):
        for n in range(1, len(list_sort)):
            if index == "":
                if list_sort[n] < list_sort[n - 1]:
                    list_sort[n - 1], list_sort[n] = list_sort[n], list_sort[n - 1]
            else:
                if list_sort[n][index] < list_sort[n - 1][index]:
                    list_sort[n - 1], list_sort[n] = list_sort[n], list_sort[n - 1]
    return list_sort


def removing(table, _id):
    """an id defined item remove from list """
    return [x for x in table if x[0] != _id]


def adding(table, add_list):
    """ ad new id element to a list"""
    _id = [generate_random(table)]
    for i in add_list:
        _id.append(i)
    while len(table[0]) > len(_id):
        _id.append("None")
    while len(table[0]) < len(_id):
        _id.pop()
    if len(table[0]) == len(_id):
        table.append(_id)
    return table


def updating(table, _id, update_list):
    index = [k for k, v in enumerate(table) if v[0] == _id]
    _id = _id.split() + update_list
    if index:
        table.append(_id)
        del table[index[0]]
        return table
    return table


def summing(sum_list):
    summa = 0
    for i in sum_list:
        summa += i
    return summa
