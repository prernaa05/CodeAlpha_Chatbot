# --- Hardcoded stock prices ---
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 300,
    "AMZN": 3300
}

# --- Welcome Message ---
print("📊 Welcome to the Stock Portfolio Tracker!")
print("Available stocks: ", ', '.join(stock_prices.keys()))
print("Enter 'done' to finish.\n")

# --- User Input Section ---
portfolio = {}
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            print("❗ Quantity must be a positive number.\n")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❗ Please enter a valid number.\n")

# --- Investment Calculation ---
print("\n📈 Calculating your total investment...\n")
total_investment = 0

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ₹{price} = ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_investment}")

# --- Optional Save to File ---
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()
if save == 'yes':
    with open("stock_portfolio_report.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("=======================\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ₹{price} = ₹{value}\n")
        file.write(f"\nTotal Investment: ₹{total_investment}\n")
    print("✅ Report saved as 'stock_portfolio_report.txt'")
else:
    print("📁 Report not saved. Done!")
