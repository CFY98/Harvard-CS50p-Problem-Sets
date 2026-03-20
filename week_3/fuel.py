def main():
    fuel = fraction("Fraction: ")
    print(fuel)

def fraction(prompt):
    while True:
        try:
            x, y = map(int, input(prompt).split('/'))  
            if x > y or y == 0 or x < 0:
                raise ValueError   
            elif (1/100) < (x / y) < (99/100):
                return f"{round((x/y)*100)}%"  
            elif (x / y) <= (1/100):
                return "E"
            elif (x / y) >= (99/100):
                return "F"
        except (ValueError, ZeroDivisionError):
            pass
main()