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
    """generate a random unique id"""
    while "generated" not in locals() or generated in [x[0] for x in table]:
        abc = [string.digits, string.ascii_uppercase, string.ascii_lowercase]
        generated = ''.join([random.choice(abc[abs(i)//2]) for i in range(-5, 6, 2)]) + "#&"
    return generated


def sorting(list_sort, index=""):
    """sorting an unsorted list (with index)"""
    for i in range(len(list_sort)):
        for n in range(1, len(list_sort)):
            if index == "":
                if list_sort[n] < list_sort[n - 1]:
                    list_sort[n - 1], list_sort[n] = list_sort[n], list_sort[n - 1]
            else:
                if list_sort[n][index].casefold() < list_sort[n - 1][index].casefold():
                    list_sort[n - 1], list_sort[n] = list_sort[n], list_sort[n - 1]
    return list_sort


def removing(table, _id):
    """an id defined item remove from list"""
    return [x for x in table if x[0] != _id]


def adding(table, add_list):
    """ ad new id element to a list"""
    return table + [[generate_random(table)] + add_list]


def updating(table, _id, update_list):
    """updating a list with modification"""
    if [x for x in table if x[0] == _id]:
        table = [x for x in table if x[0] != _id] + [[_id] + update_list]
    return table


def summing(sum_list):
    """sum of a list"""
    summa = 0
    for i in sum_list:
        summa += i
    return summa
