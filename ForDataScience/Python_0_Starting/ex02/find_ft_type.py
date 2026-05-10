#!/usr/bin/env python3

def all_thing_is_obj(object: any) -> int:
    """
    This function prints the type of the object passed as an argument and returns 42.
    """

    if type(object) == list:
        print("List :", type(object))
    elif type(object) == tuple:
        print("Tuple :", type(object))
    elif type(object) == set:
        print("Set :", type(object))
    elif type(object) == dict:
        print("Dict :", type(object))
    elif type(object) == str:
        print(object, "is in the kitchen :", type(object))
    else:
        print("Type not found.")
    return 42
