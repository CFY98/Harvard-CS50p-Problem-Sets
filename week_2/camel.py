def nametype():
    camels = ["name", "first_name", "preferred_first_name"]
    x = input("camelCase: ").strip()
    
    if x == "name":
        print("snake_case:", camels[0])
    elif x == "firstName":
        print("snake_case:", camels[1])
    elif x == "preferredFirstName":
        print("snake_case:", camels[2])
    else:
        pass

nametype()


