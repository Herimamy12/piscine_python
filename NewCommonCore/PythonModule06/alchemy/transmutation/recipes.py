from elements import create_fire
from alchemy.elements import create_air, create_earth

def lead_to_gold():
    return f"Recipe transmuting Lead to Gold: brew ’{create_air()}’ and ’{create_earth()}’ mixed with ’{create_fire()}’"
