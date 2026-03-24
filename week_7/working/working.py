import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
        if not " to " in s:
             raise ValueError
        entry = re.split(r" to ", s)
        return f"{parse(entry[0])} to {parse(entry[1])}"

def parse(entry):
        hours = re.fullmatch(r"(0?[1-9]|1[0-2])(?::([0-5][0-9]))? +(am|pm)", entry.strip(), flags=re.IGNORECASE)
        if not hours:
             raise ValueError
        hour = int(hours.group(1))
        minutes = hours.group(2) or "00"
        time = hours.group(3).upper()

        if time == "AM" and hour == 12:
            hour = 0
        elif time == "PM" and hour != 12:
            hour += 12
        return f"{hour:02d}:{minutes}"

if __name__ == "__main__":
    main()
