def main():
    grocery = {}
    while True:
        try:
            k = input().upper()
            if k in grocery:
                grocery[k] += 1
            else:
                grocery[k] = 1
        except (EOFError, KeyError):
            for k in sorted(grocery):
                print(grocery.get(k), k)
            break
main()
