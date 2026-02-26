import sys
import csv

def main():
    try:
        if len(sys.argv) > 3:
            sys.exit('Too many command-line arguments')
        elif len(sys.argv) < 3:
            sys.exit('Too few command-line arguments')
        else:
            if not sys.argv[1].endswith('.csv'):
                sys.exit('Not a CSV file')
            else:
                file = sys.argv[1]
                new_file = sys.argv[2]
                modify(file, new_file)
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

def modify(file, new_file):
    student = []
    with open(file, 'r') as source:
        reader = csv.DictReader(source)
        for line in reader:
            last, first = line["name"].split(', ')
            house = line["house"].strip()
            student.append({"first": first, "last": last, "house": house})

    with open(new_file, 'w', newline='') as result:
        writer = csv.DictWriter(result, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for row in student:
            writer.writerow(row)
        return writer

if __name__ == "__main__":
    main()
