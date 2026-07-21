# Hardcoded dictionary containing stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOG": 170,
    "AMZN": 190
}

# Display available stocks
print("=" * 50)
print("Available Stocks")
print("=" * 50)

for key, value in stocks.items():
    print(f"{key} : ${value}")

# Get number of different stocks the user wants to buy
while True:
    try:
        no_of_stocks = int(input("\nHow many different stocks do you want to buy? "))
        if no_of_stocks > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

total_investment = 0
chosen_stock = {}

# Collect stock details
for i in range(no_of_stocks):

    # Validate stock symbol
    while True:
        stock_symbol = input("\nEnter stock symbol: ").upper()

        if stock_symbol in stocks:
            break
        else:
            print("Invalid stock symbol! Please try again.")

    # Validate quantity
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                break
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid quantity.")

    investment = quantity * stocks[stock_symbol]
    total_investment += investment

    # If stock already exists, update quantity and investment
    if stock_symbol in chosen_stock:
        chosen_stock[stock_symbol][0] += quantity
        chosen_stock[stock_symbol][1] += investment
    else:
        chosen_stock[stock_symbol] = [quantity, investment]

# Display portfolio summary
print("\n" + "=" * 50)
print("Portfolio Summary")
print("=" * 50)

for stock, details in chosen_stock.items():
    print(f"Stock       : {stock}")
    print(f"Quantity    : {details[0]}")
    print(f"Price       : ${stocks[stock]}")
    print(f"Investment  : ${details[1]}")
    print("-" * 50)

print(f"Total Investment: ${total_investment}")

# Ask user whether to save the portfolio
save = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_summary.txt", "w") as file:

        file.write("=" * 50 + "\n")
        file.write("Portfolio Summary\n")
        file.write("=" * 50 + "\n")

        for stock, details in chosen_stock.items():
            file.write(f"Stock       : {stock}\n")
            file.write(f"Quantity    : {details[0]}\n")
            file.write(f"Price       : ${stocks[stock]}\n")
            file.write(f"Investment  : ${details[1]}\n")
            file.write("-" * 50 + "\n")

        file.write(f"Total Investment: ${total_investment}\n")

    print("\nPortfolio saved successfully as 'portfolio_summary.txt'.")

else:
    print("\nPortfolio was not saved.")
