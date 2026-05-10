#!/usr/bin/env/ python3

def cout(number, value):
    print(value)
    if (number > 0):
        value += 1
        number -= 1
        cout(number, value)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: ")) - 1
    out = 1
    cout(days, out)
    print("Harvest time!")
