import alchemy.grimoire.dark_validator as dark_validator
import alchemy.grimoire.dark_spellbook as dark_spellbook


def record_dark_spell(spell_name: str, ingredients: str):
    """
    A function record_dark_spell(spell_name: str, ingredients: str) that records a dark
    spell using the dark_spell_record() function from the dark_spellbook module.
    """
    return dark_spellbook.dark_spell_record(spell_name, ingredients)


if __name__ == "__main__":
    # Example usage with a true dark spell
    spell_name = "Shadow Bind"
    ingredients = "bats"
    result = record_dark_spell(spell_name, ingredients)
    print(result)
    result_validation = dark_validator.validate_ingredients(ingredients)
    print(result_validation)

    # Example usage with an invalid dark spell
    spell_name = "Light Burst"
    ingredients = "earth"
    result = record_dark_spell(spell_name, ingredients)
    print(result)
    result_validation = dark_validator.validate_ingredients(ingredients)
    print(result_validation)
