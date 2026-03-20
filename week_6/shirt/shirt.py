import sys, os
from PIL import Image, ImageOps

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        else:
            input = os.path.splitext(sys.argv[1])
            output = os.path.splitext(sys.argv[-1])
            if input[1] not in [".jpeg", ".jpg", ".png"] or output[1] not in [".jpeg", ".jpg", ".png"]:
                sys.exit("Invalid input")
            elif input[1] != output[1]:
                sys.exit("Input and output have different extensions")
            else:
                muppet = sys.argv[1]
                shirted = sys.argv[2]
                clothes(muppet, shirted)
    except FileNotFoundError:
        sys.exit("File not found")

def clothes(muppet, shirted):
    with Image.open(muppet) as model:
        shirt = Image.open("shirt.png")
        fitting = ImageOps.fit(model, shirt.size)
        fitting.paste(shirt, shirt)
        fitting.convert("RGB").save(shirted)

if __name__ == "__main__":
    main()
