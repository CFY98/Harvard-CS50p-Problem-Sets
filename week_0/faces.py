def main():
    emoji = input()
    print(convert(emoji))

def convert(emoji):
    return emoji.replace(":)", "🙂").replace(":(", "🙁")

main()
