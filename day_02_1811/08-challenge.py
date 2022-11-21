from day_02_1811.utils import caesar_shift

# Day 02 challenge - Ceasar's Cipher
# Lets jump into crypto right away! Use the easiest cryptographic mechanism to create an encrypted message!
# refer to: https://en.wikipedia.org/wiki/Caesar_cipher
# - Your input is a sentence
# - Encode with Caesar
# - Return the sentence

# Examples:
# 'THE' -> 'QEB'
# 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG' -> 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'

# This is the main file, checking your solution
# Write your solution in utils.py

# !!One-up challenge!!
# Split your solution into more atomic functions for easy testing
# Apart from encoder (standard to Caesar) -> write the decoder (Caesar to standard)
# But actually can the encoder and decoder be the same function?
# Rewrite the asserts below using pytest


if __name__ == '__main__':
    assert(caesar_shift("THE", "encoder") == "QEB")
    print('Test 01 - ok!')
    assert(caesar_shift("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", "encoder") == "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD")
    print('Test 02 - ok!')
    assert(caesar_shift("DAO", "encoder") == "AXL")
    print('Test 02 - ok!')
    assert(caesar_shift("QEB", "decoder") == "THE")
    print('Test 01 - ok!')
    assert(caesar_shift("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD", "decoder") == "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
    print('Test 02 - ok!')
