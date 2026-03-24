import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        if re.fullmatch(r"^\d+(\.\d+){3}$", ip):
            octet = ip.split(".")
            for i in octet:
                n = int(i)
                if n < 0 or n > 255:
                    return False
                if len(i) > 1 and i[0] == "0":
                    return False
            return True
        return False
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    main()
