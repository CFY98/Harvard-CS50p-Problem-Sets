from datetime import date
import re
import sys
import inflect

class Minutes:
    def __init__(self, minutes):
        self.minutes = minutes

    def __str__(self):
        p = inflect.engine()
        return f"{p.number_to_words(self.minutes, andword='')} {p.plural_noun('minute', self.minutes)}".capitalize()

    def __sub__(self, other):
        age = self.minutes - other.minutes
        return Minutes(age)

    @classmethod
    def minutes(cls, birthday=None):
        if birthday is None:
            birthday = input("Date of Birth: ")

        valid = re.match(r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[0-2][0-9]|3[0-1])$", birthday)
        if not valid:
            sys.exit("Invalid Date")

        year, month, day = map(int, valid.groups())

        birth_date = date(year, month, day)
        now = date.today()
        difference = now - birth_date
        minutes = difference.days * 24 * 60

        return cls(minutes)

def main():
    minutes = Minutes.minutes()
    print(minutes)


if __name__ == "__main__":
    main()
