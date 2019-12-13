#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: Dec 2019
# This program uses a 2D array

import random


def sum_of_numbers(passed_in_2D_list, rows, columns):
    # this function adds up all the elements in  a 2D array

    total = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element
    total = total/(rows*columns)
    return total


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    rows = (input("How many row would you like: "))
    columns = (input("How many columns would you like: "))
    try:
        rowsInt = int(rows)
        columnsInt = int(columns)
        for loop_counter_rows in range(0, rowsInt):
            temp_column = []
            for loop_counter_columns in range(0, columnsInt):
                a_random_number = random.randint(1, 50)
                temp_column.append(a_random_number)
                print("{0} ".format(a_random_number), end="")
            a_2d_list.append(temp_column)
            print("")

        sum = sum_of_numbers(a_2d_list, rowsInt, columnsInt)
        print("The average of all the numbers is: {0} ".format(sum))
    except Exception:
        print("invalid integer")


if __name__ == "__main__":
    main()
