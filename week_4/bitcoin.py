import sys
import requests

def isdigit(arg):
    try:
        if float(arg) > 0:
            return True
        else:
            sys.exit('Number must be higher than 0.')
    except ValueError:
        return False

try:
    r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=f132bbafad103221c5e99516ca6a0e071cd68b6945af16a51665b6378fe531a9')
    if len(sys.argv) < 2:
        sys.exit('Missing command-line argument')

    arg = sys.argv[1]

    if isdigit(arg) == False:
        sys.exit('Command-line argument is not a number.')
    elif isdigit(arg) == True:
        data = r.json()
        price = data["data"]["priceUsd"]
        amount = float(price)*float(arg)
        print(f'${amount:,.4f}')
except requests.RequestException:
    sys.exit()
