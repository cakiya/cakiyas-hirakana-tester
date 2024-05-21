"""
This program picks a random hirakana romaji and displays
it to the user (so they can write down the corresponding
hiragana and katakana as practice) and keeps on going until
every hirakana romaji has been tested; then it exits once the
test is done, im too lazy to implement retry feature
"""

import random

GLOBALVAR_ROMAJI = [
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

GLOBALVAR_HIRAGANA = [
   "あ", "い", "う", "え", "お",
   "か", "き", "く", "け", "こ",
   "さ", "し", "す", "せ", "そ",
   "た", "ち", "つ", "て", "と",
   "な", "に", "ぬ", "ね", "の",
   "は", "ひ", "ふ", "へ", "ほ",
   "ま", "み", "む", "め", "も",
   "や", "ゆ", "よ",
   "ら", "り", "る", "れ", "ろ",
   "わ", "を", "ん"
]

GLOBALVAR_KATAKANA = [
    "ア", "イ", "ウ", "エ", "オ",
    "カ", "キ", "ク", "ケ", "コ",
    "サ", "シ", "ス", "セ", "ソ",
    "タ", "チ", "ツ", "テ", "ト",
    "ナ", "ニ", "ヌ", "ネ", "ノ",
    "ハ", "ヒ", "フ", "ヘ", "ホ",
    "マ", "ミ", "ム", "メ", "モ",
    "ヤ", "ユ", "ヨ",
    "ラ", "リ", "ル", "レ", "ロ",
    "ワ", "ヲ", "ン"
]

# "class" variables
global Romaji 
global Hiragana
global Katakana
global Hirakana_count

def fill_lists():
    """
    refills global variables Romaji, Hiragana, Katakana
    note: Romaji, Hiragana, Katakana are list[str] type.
    """
    global Romaji
    global Hiragana
    global Katakana
    global Hirakana_count
    # Modifies the global variables
    Romaji = GLOBALVAR_ROMAJI.copy()
    Hiragana = GLOBALVAR_HIRAGANA.copy() 
    Katakana = GLOBALVAR_KATAKANA.copy()   
    Hirakana_count = len(Romaji) # should be 46

def test_loop():
    """
    main test loop. this is the actual code that tests
    the user on hiragana/katakana.
    """
    global Romaji
    global Hiragana
    global Katakana
    global Hirakana_count
    print("====================================")
    print("This test will show you the Romaji of a Hirakana character.")
    print("Please write it in Hiragana and Katakana.")
    print("Press [Enter] to move to the next question.")
    print("====================================")
    for i in range(Hirakana_count):
        hirakana_tuple = get_hirakana() # (Romaji, Hiragana, Katakana)
        print("Hirakana ", i+1, ": ", hirakana_tuple[0], sep='', end='')
        input('')[: -1]
        print('  (h) (k)  ', hirakana_tuple[1], ' ', hirakana_tuple[2])
        
       
        
        

def get_hirakana():
    """
    chooses and removes a random hirakana tuple from
    the hirakana list 
    format: (Romaji, Hiragana, Katakana)
    """
    global Romaji
    global Hiragana
    global Katakana
    random_index = random.randint(0, len(Romaji)-1)
    chosen_romaji = Romaji.pop(random_index)
    chosen_hiragana = Hiragana.pop(random_index)
    chosen_katakana = Katakana.pop(random_index)
    return chosen_romaji, chosen_hiragana, chosen_katakana

def main():
    fill_lists()
    print("BEGINNING TEST")
    test_loop()

# Don't forget to call main()!
main()
