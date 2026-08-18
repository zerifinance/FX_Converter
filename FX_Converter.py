print()
print("Currency: USD")
amount=float(input("Amount: "))
print()

print("Today's USD Exchange Rate: ")
buy=float(input("Buy Rate: "))
sell=float(input("Sell Rate: "))
print()

print("Please choose: ")
print("1. Sell USD")
print("2. Buy USD\n")

choice=float(input("Your choice: "))
print()
if choice==1:
    print(f"Amount in TWD: {amount*buy:,.0f}")
elif choice==2:
    print(f"Amount in TWD: {amount*sell:,.0f}")
