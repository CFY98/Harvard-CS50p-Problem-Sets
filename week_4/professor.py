import random

def main():
    correct = 0
    level = get_level()

    for s in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y

        attempts = 0
        while attempts < 3:
            try:
                maths = int(input(f'{x} + {y} = '))
                if maths != result:
                    print('EEE')
                    attempts += 1
                else:
                    correct += 1
                    break
            except ValueError:
                print('EEE')
                attempts += 1
        if attempts == 3:
            print(f'{x} + {y} = {x+y}')

    print(f'Score: {correct}')

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        n = random.randrange(0, 10)
    elif level == 2:
        n = random.randrange(10, 100)
    else:
        n = random.randrange(100, 1000)
    return n

if __name__ == "__main__":
    main()
