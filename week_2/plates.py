def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #vanity plates must have a minimum of two characters, max 6.
    if not (2 <= len(s) <=6):
        return False
    
    #vanity plate must begin with 2 letters
    if not s[:2].isalpha():
        return False

    #vanity plates must not have punctuation or spaces.
    for char in s:
        if char in [".", ",","?"," ","!"]:
            return False
    return sans_mid_num(s)
    
def sans_mid_num(s):
    for i, char in enumerate(s):
        if char.isnumeric():
            #first number cannot be 0:
            if char == "0": 
                return False
            #everything after must be a number:
            return s[i:].isnumeric() 
    return True

main()
