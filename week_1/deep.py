question = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").casefold().strip()

match question:
    case str("42") | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

