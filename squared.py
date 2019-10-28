#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: OCT 2019
# This program uses a while loop


def count():
    # this function uses a for loop
    answer = 0

    # input
    positive_integer = input("Enter A Positive Number (+) : ")
    print("")

    # process & output
    try:
        positive_integer_num = int(positive_integer)
        for loop_counter in range(1, positive_integer_num+1):
            answer = loop_counter ** 2
            print("{0}**2 = {1}".format(loop_counter, answer))

    except ValueError:
            print()
            print("Invalid Input")


if __name__ == "__main__":
    count()
