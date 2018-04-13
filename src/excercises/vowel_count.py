def getCount(inputStr):
    num_vowels = 0
    vowels = "aeiou"
    for vowel in vowels:
        num_vowels += inputStr.count(vowel)

    return num_vowels

print(getCount("abracadabra"))