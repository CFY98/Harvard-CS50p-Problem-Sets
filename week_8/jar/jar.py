class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0
    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError
        self._size += n
    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError
        self._size -= n
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()

    while True:
        action = input("What to do with Cookie Jar? [Take, Store, Count, Quit] " ).casefold()

        if action == "take":
            try:
                n = int(input("How many? "))
                jar.withdraw(n)
                print("👹" * n)
            except ValueError:
                print("The jar doesn't have enough cookies")
        elif action == "store":
            try:
                n = int(input("How many? "))
                jar.deposit(n)
                print("🍪" * n)
            except ValueError:
                print("This exceeds the capacity")
        elif action == "count":
            print(jar)
        else:
            break

if __name__ == "__main__":
    main()
