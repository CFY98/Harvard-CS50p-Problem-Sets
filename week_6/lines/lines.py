import sys

def check():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            if not sys.argv[1].endswith(".py"):
                sys.exit("Not a Python File")
            else:
                with open(sys.argv[1], "r") as file:
                    num_of_lines = sum(1 for line in file if not line.lstrip().startswith("#") and line.strip())
                    print(num_of_lines)

    except FileNotFoundError:
        sys.exit("File does not exist.")

check()





