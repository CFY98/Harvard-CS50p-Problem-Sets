# import string

def main():
    word = input("Input: ")
    result = shorten(word)
    print(result)


def shorten(word):
    vowels = "aeiou"
    # numbers = "0123456789"
    # punct = string.punctuation
    output = ""
    for vowel in word:
        if vowel.lower() not in vowels:
            output += vowel

    # for number in word:
    #     if number in numbers:
    #         output = output.replace(number, "")

    # for pun in word:
    #     if pun in punct:
    #         output = output.translate(output.maketrans("", "", punct))

    return output


if __name__ == "__main__":
    main()
