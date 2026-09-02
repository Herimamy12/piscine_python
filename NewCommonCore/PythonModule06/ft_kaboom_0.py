import alchemy.grimoire as grimoire


def record_light_spell(spell_name: str, ingredients: str):
    """
    A function record_light_spell(spell_name: str, ingredients: str) that records a light
    spell using the light_spell_record() function from the light_spellbook module.
    """
    return grimoire.light_spell_record(spell_name, ingredients)


if __name__ == "__main__":
    # Example usage with a true light spell
    spell_name = "Healing Light"
    ingredients = "earth"
    result = record_light_spell(spell_name, ingredients)
    print(result)

    # Example usage with an invalid light spell
    spell_name = "Dark Flame"
    ingredients = "bats"
    result = record_light_spell(spell_name, ingredients)
    print(result)
