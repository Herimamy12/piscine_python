#!/usr/bin/env/ python3

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    pref_ix: str
    suff_ix: str
    if (unit == "packets"):
        pref_ix = seed_type.capitalize() + " seeds:"
        suff_ix = "packets available"
    elif (unit == "grams"):
        pref_ix = seed_type.capitalize() + " seeds:"
        suff_ix = "grams total"
    elif (unit == "area"):
        pref_ix = seed_type.capitalize() + " seeds: covers"
        suff_ix = "square meters"
    else:
        print("Unknown unit type")
        return
    print(pref_ix, quantity, suff_ix, sep=" ")
