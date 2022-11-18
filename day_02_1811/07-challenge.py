from day_02_1811.utils import reverse_words

# Day 02 challenge - Tongue Twister
# - You are given a sentence.
# - Find the words that are longer than 4 letters.
# - Reverse their order
# - Return the sentence

# Examples:
# 'Hey' -> 'Hey'
# 'Challenge' -> 'egnellahC'
# 'Challenges are finally here' -> 'segnellahC are yllanif here'

# This is the main file, checking your solution
# Write your solution in utils.py

if __name__ == '__main__':
    assert(reverse_words("Hey!") == "Hey!")
    print('Test 01 - ok!')
    assert(reverse_words("Challenges") == "segnellahC")
    print('Test 02 - ok!')
    assert(reverse_words("are") == "are")
    print('Test 03 - ok!')
    assert(reverse_words("finally here") == "yllanif here")
    print('Test 04 - ok!')
    assert(reverse_words("Lets get the learning started") == "Lets get the gninrael detrats")
    print('Test 05 - ok!')
