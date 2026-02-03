import random

def answer(integer):
    while True:
        try:
            guess = int(input('Guess: '))
            if guess <= 0:
                continue
            if guess > integer:
                print('Too large!')
                continue
            elif guess < integer:
                print('Too small!')
                continue
            else:
                print('Just right!')
                break
        except ValueError:
            continue

def main():
    while True:
        try:
            level = int(input('Level: '))
            if 1 <= level <= 100:
                integer = random.randint(1, 100)
                answer(integer)
            else:
                continue
        except ValueError:
            continue
        break

if __name__ == "__main__":
	main()


