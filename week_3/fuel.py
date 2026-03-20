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

# Abstraction:
# def main():
#     fuel_fraction = get_valid_fraction("Fraction: ")
#     fuel_level = convert_to_fuel_level(fuel_fraction)
#     print(fuel_level)

# def get_valid_fraction(prompt):
#     while True:
#         try:
#             x, y = map(int, input(prompt).split('/'))
#             if y == 0 or x > y or x < 0:
#                 raise ValueError
#             return x / y  # return as float for further processing
#         except (ValueError, ZeroDivisionError):
#             pass

# def convert_to_fuel_level(fraction_value):
#     if fraction_value <= 0.01:
#         return "E"
#     elif fraction_value >= 0.99:
#         return "F"
#     else:
#         return f"{round(fraction_value * 100)}%"
    
# main()
