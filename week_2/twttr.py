words = input("Input: ")
vowels = "aeiou"
output = ""

for vowel in words:
    if vowel.lower() not in vowels:
        output += vowel

print(output)

