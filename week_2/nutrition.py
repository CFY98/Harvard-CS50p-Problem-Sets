def main():
    food = input("Item: ").casefold()
    fruits = [
        {"fruit": "strawberry", "calories": 50}, 
        {"fruit": "apple", "calories": 130}, 
        {"fruit": "banana", "calories": 110}, 
        {"fruit": "avocado", "calories": 50}, 
        {"fruit": "sweet cherries", "calories": 100},
        {"fruit": "kiwifruit", "calories": 90},
        {"fruit": "pear", "calories": 100},
    ]

    #print calories of the specific fruit in the dictionary.
    for fruit in fruits:
        if fruit["fruit"] in food:
            print("Calories:", fruit["calories"])
        else:
            pass
            
main()



