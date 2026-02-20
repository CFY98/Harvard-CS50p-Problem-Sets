def main():
    greeting = input("Greeting: ").lower()
    print(f"${value(greeting)}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h", 0):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
