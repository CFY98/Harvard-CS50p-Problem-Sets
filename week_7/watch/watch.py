import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if src := re.search(r'src="(https?://)?(?:www\.)?youtube\.com/embed/([\w]+)"></iframe>', s):
        return f"https://youtu.be/{src.group(2)}"
    return None


if __name__ == "__main__":
    main()
