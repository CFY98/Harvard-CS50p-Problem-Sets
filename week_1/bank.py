def main():
    cash = input("Greeting: ").lower().strip()

    if cash.startswith("hello"):
        print("$0")
    elif cash.startswith("h", 0):
        print("$20")
    else:
        print("$100")

main()
