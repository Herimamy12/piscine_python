from .light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str):
    """
    A function validate_ingredients(ingredients: str) that returns a string with
    the ingredients and the “VALID” or “INVALID” keyword. The ingredients are
    valid if they include at least one of the allowed ingredients from the spellbook (case
    insensitive).
    """
    allowed_ingredients = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    for ingredient in allowed_ingredients:
        if ingredient.lower() in ingredients_lower:
            return f"Ingredients: {ingredients} - VALID"
    return f"Ingredients: {ingredients} - INVALID"
