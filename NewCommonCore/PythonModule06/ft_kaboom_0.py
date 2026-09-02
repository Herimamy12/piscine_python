# ft_kaboom_0.py will access the grimoire module directly and then record a light
# spell, flawlessly. There are multiple ways to avoid circular dependencies; you pick
# one. Be prepared to explain the different approaches during the evaluation.

import alchemy.grimoire.light_spellbook as light_spellbook


def record_light_spell(spell_name: str, ingredients: str):
    """
    A function record_light_spell(spell_name: str, ingredients: str) that records a light
    spell using the light_spell_record() function from the light_spellbook module.
    """
    return light_spellbook.light_spell_record(spell_name, ingredients)


if __name__ == "__main__":
    # Example usage with a true light spell
    spell_name = "Healing Light"
    ingredients = "earth"
    result = record_light_spell(spell_name, ingredients)
    print(result)  # Output: The spell 'Healing Light' with ingredient 'earth' is recorded.

    # Example usage with an invalid light spell
    spell_name = "Dark Flame"
    ingredients = "bats"
    result = record_light_spell(spell_name, ingredients)
    print(result)  # Output: The spell 'Dark Flame' with ingredient 'bats' is rejected. Invalid ingredient.
