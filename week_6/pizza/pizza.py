import sys
import tabulate
import csv

def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        else:
            if not sys.argv[1].endswith(".csv"):
                sys.exit("Not a CSV file")
            else:
                filename = sys.argv[1]
                print(menu(filename))
    except FileNotFoundError:
        sys.exit("File does not exist")

def menu(filename):
    with open(filename) as source:
        reader = csv.reader(source)
        table = list(reader)
        headers = list(source.readline())
        return tabulate.tabulate(table, headers="firstrow", tablefmt="grid")

if __name__ == "__main__":
    main()
