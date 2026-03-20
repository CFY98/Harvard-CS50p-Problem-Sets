from pyfiglet import Figlet
import sys
from random import choice

f = Figlet()
fonts = f.getFonts()

try:
    if len(sys.argv) == 1:
        c = choice(fonts)
        f.setFont(font=c)
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            raise ValueError("Invalid Usage")
        if sys.argv[2] not in fonts:
            raise ValueError("Invalid Usage")
        elif sys.argv[2] in fonts:
            f.setFont(font=sys.argv[2])
    else:
        raise IndexError("Invalid Usage")
except (IndexError, ValueError) as e:
    sys.exit(e)

x = input('Input: ')
print('Output:\n\n', f.renderText(x))



