# implement commonly used functions here
# import data_manager
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


def sorting(list_sort):
    for i in range(len(list_sort)):
        for n in range(1, len(list_sort)):
            if list_sort[n] < list_sort[n - 1]:
                list_sort[n - 1], list_sort[n] = list_sort[n], list_sort[n - 1]
    return list_sort


def removing(table, _id):
    table_list = [v for k, v in enumerate(table)]
    index = [k for k, v in enumerate(table) if v[0] == _id]
    del table_list[index[0]]
    return table_list
