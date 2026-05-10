#!/usr/bin/env python3

def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None", type(object))
        return 0
    elif type(object) == float and object != object:
        print("Cheese: nan", type(object))
        return 0
    elif object is False:
        print("Fake: False", type(object))
        return 0
    elif object == 0:
        print("Zero: 0", type(object))
        return 0
    elif object == "":
        print("Empty:", type(object))
        return 0
    print("Type not found")
    return 1