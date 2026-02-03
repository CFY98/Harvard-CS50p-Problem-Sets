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
    
#COULD CONSIDER:
#def nametype():
   #camel = input("camelCase: ")
   #snake = convert(camel)
   #print("snakecase:", snake)
   
#def convert(camel):
   #snake = "" #empty string to be built by going through the below loop*
   #for case in camel:
       #if case.isupper():
           #snake += "_" + case.lower() #lowercases the uppercase character with underscore added before it.
       #else:
           #snake += case
   #return snake #this returns the newly built string after it's gone through the loop.*

nametype()

    




