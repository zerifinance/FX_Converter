import json
import sys
import requests

print("Currency: USD")
amount=float(input("Amount: "))
print()

currency=input("Which currency would you like to convert to? ex.EUR, JPY, TWD ").upper()
ex=requests.get("https://api.exchangerate.fun/latest")
data=ex.json()
rates=data["rates"]
rate=rates[currency]

print(f"Amount in {currency}: {amount*rate:,.2f}")
