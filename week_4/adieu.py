import inflect

p = inflect.engine()
names = []

while True:
    try:
        print("Name:")
        name = input().title()
        if name == '':
            continue
        if name not in names:
            names.append(name)
    except (EOFError):
        print(f'Adieu, adieu, to {p.join(names)}')
        break







