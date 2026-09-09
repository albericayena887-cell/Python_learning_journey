import sys
import requests


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")


try:
    quantity = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
   
    response = requests.get("https://coindesk.com")
    data = response.json()
    
    
    bitcoin_price = data["bpi"]["USD"]["rate_float"]
    
   
    total_amount = quantity * bitcoin_price
    
    
    print(f"${total_amount:,.4f}")

except requests.RequestException:
    
    sys.exit("Error fetching Bitcoin price")
