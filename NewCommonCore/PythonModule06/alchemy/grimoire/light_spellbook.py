def light_spell_allowed_ingredients():
    """
    A function light_spell_allowed_ingredients() that returns a list of allowed
    ingredients for light magic, let’s say “earth”, “air”, “fire”, “water”.
    """
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str):
    """
    A function light_spell_record(spell_name: str, ingredients: str) that re-
    turns a string that indicates whether the spell is recorded or rejected. The decision
    comes from the validation function described below.
    """
    allowed_ingredients = light_spell_allowed_ingredients()
    if ingredients in allowed_ingredients:
        return f"The spell '{spell_name}' with ingredient '{ingredients}' is recorded."
    else:
        return f"The spell '{spell_name}' with ingredient '{ingredients}' is rejected. Invalid ingredient."
