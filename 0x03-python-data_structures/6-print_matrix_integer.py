#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for each_row in matrix:
        row_size = len(each_row)
        for idx in range(row_size):
            if idx == row_size - 1:
                print("{:d}".format(each_row[idx]), end="")
            else:
                print("{:d}".format(each_row[idx]), end=" ")
        print("")
