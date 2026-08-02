print("Currency: USD")
amount=float(input("Amount: "))
print()

print("今天 USD 匯率: ")
buy=float(input("Buy: "))
sell=float(input("Sell: "))
print()

print("請選擇: ")
print("1. 我要賣美金")
print("2. 我要買美金\n")

choice=float(input("您的選擇是: "))
print()
if choice==1:
    print(f"TWD: {amount*buy:,.2f}")
elif choice==2:
    print(f"TWD: {amount*sell:,.2f}")
