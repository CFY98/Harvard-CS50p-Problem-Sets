def convert(date):
    month, day, year = date.split("/")
    month = int(month)
    day = int(day)
    year = int(year)
    if not (1 <= month <= 12) or not (1 <= day <= 31):
        raise ValueError
    return month, day, year

def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:
        try:
            date = input("Date: ").strip().title()
            month, day, year = convert(date)
        except(ValueError, IndexError):
            try: 
                parts = date.split(",")
                if len(parts) != 2:
                    continue

                year = int(parts[1].strip())
                day = int(parts[0].split(" ")[1].replace(",", ""))
                if day > 31:
                        continue
                
                month_name = parts[0].split(" ")[0]
                if month_name in months:
                    month = months.index(month_name) + 1
                else:
                    pass

            except(ValueError, IndexError):
                continue
        print(f"{year}-{month:02}-{day:02}")
        break

main()