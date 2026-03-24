import validators

def main():
    print(validate(input("What's your email address? ")))

def validate(email):
    if not validators.email(email):
        return "Invalid"
    return "Valid"

if __name__ == "__main__":
    main()

