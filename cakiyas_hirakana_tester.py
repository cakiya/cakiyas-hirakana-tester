"""
This program picks a random hirakana romaji and displays
it to the user (so they can write down the corresponding
hiragana and katakana as practice) and keeps on going until
every hirakana romaji has been tested; then it crashes becasue
i dont know im too lazy to implement not crashing and re-usability
"""


import random

GLOBALVAR_HIRAKANA_ROMAJI = [
    "a", "i", "u", "e", "o",
    "ka", "ki", "ku", "ke", "ko",
    "sa", "shi", "su", "se", "so",
    "ta", "chi", "tsu", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo",
    "ra", "ri", "ru", "re", "ro",
    "wa", "wo", "n"
]

test_list = GLOBALVAR_HIRAKANA_ROMAJI.copy()

print(GLOBALVAR_HIRAKANA_ROMAJI)

def test_loop():
    hirakana_count = len(GLOBALVAR_HIRAKANA_ROMAJI)
    for i in range(hirakana_count):
        print("Hirakana", i+1, ":", test_one_hirakana())
        input("Press enter to Proceed")

def test_one_hirakana():
    """
    chooses and removes a random hirakana from
    the hirakana list
    """
    random_hirakana_in_list = random.randint(0, len(test_list)-1)
    return test_list.pop(random_hirakana_in_list)

def main():
    print("BEGINNING TEST")
    test_loop()

# Don't forget to call main()!
main()