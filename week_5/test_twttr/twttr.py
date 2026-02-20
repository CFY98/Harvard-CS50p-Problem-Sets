def main():
    word = input("Input: ")
    result = shorten(word)
    print(result)


def shorten(word):
    vowels = "aeiou"
    output = ""
    for vowel in word:
        if vowel.lower() not in vowels:
            output += vowel
    return output


if __name__ == "__main__":
    main()
