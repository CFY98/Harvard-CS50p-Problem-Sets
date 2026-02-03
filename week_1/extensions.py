def extensions():
    file = input("File name: ").casefold().strip()
    pic = (".gif", ".png")
    photo = (".jpg", ".jpeg")
    app = (".pdf", ".zip")
    doc = (".txt")

    if file.endswith(pic):
        print(f"image/{file.rsplit(".", 1)[-1]}")
    elif file.endswith(photo):
        print("image/jpeg")
    elif file.endswith(app):
        print(f"application/{file.rsplit(".", 1)[-1]}")
    elif file.endswith(doc):
        print("text/plain")
    else:
        print("application/octet-stream")

extensions()
