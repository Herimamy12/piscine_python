def dark_spell_allowed_ingredients():
    """
    A function dark_spell_allowed_ingredients() that returns a list of allowed
    ingredients for dark magic, let’s say  “bats”, “frogs”, “arsenic”, and “eyeball”.
    """
    return ["bats", "frogs", "arsenic", "eyeball"]

def dark_spell_record(spell_name: str, ingredients: str):
    """
    A function dark_spell_record(spell_name: str, ingredients: str) that re-
    turns a string that indicates whether the spell is recorded or rejected. The decision
    comes from the validation function described below.
    """
    allowed_ingredients = dark_spell_allowed_ingredients()
    if ingredients in allowed_ingredients:
        return f"The spell '{spell_name}' with ingredient '{ingredients}' is recorded."
    else:
        return f"The spell '{spell_name}' with ingredient '{ingredients}' is rejected. Invalid ingredient."
