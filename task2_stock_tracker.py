# ===========================================================
# CodeAlpha Internship — Task 2: Stock Portfolio Tracker
# ===========================================================

import csv
import os

# Hardcoded stock prices (as required by the task)
STOCK_PRICES = {
    "AAPL":  182.50,   # Apple
    "TSLA":  248.00,   # Tesla
    "GOOGL": 175.30,   # Google
    "MSFT":  415.00,   # Microsoft
    "AMZN":  192.80,   # Amazon
    "NFLX":  645.00,   # Netflix
    "META":  520.00,   # Meta
    "INFY":   19.50,   # Infosys (Indian stock)
    "TCS":    43.00,   # TCS (Indian stock)
    "WIPRO":  10.20,   # Wipro (Indian stock)
}


def show_available_stocks():
    print("\n📈 Available Stocks:")
    print("-" * 35)
    print(f"{'Symbol':<10} {'Company':<15} {'Price (USD)'}")
    print("-" * 35)
    companies = {
        "AAPL": "Apple", "TSLA": "Tesla", "GOOGL": "Google",
        "MSFT": "Microsoft", "AMZN": "Amazon", "NFLX": "Netflix",
        "META": "Meta", "INFY": "Infosys", "TCS": "TCS", "WIPRO": "Wipro"
    }
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10} {companies[symbol]:<15} ${price:.2f}")
    print("-" * 35)


def get_portfolio():
    portfolio = {}
    print("\n📝 Enter your stock holdings (type 'done' when finished):")

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

        if stock == "DONE":
            if not portfolio:
                print("⚠️  You haven't added any stocks yet.")
                continue
            break

        if stock not in STOCK_PRICES:
            print(f"❌ '{stock}' not found. Please choose from the available list.")
            continue

        try:
            qty = int(input(f"Enter quantity for {stock}: "))
            if qty <= 0:
                print("⚠️  Quantity must be a positive number.")
                continue
        except ValueError:
            print("⚠️  Please enter a valid number.")
            continue

        if stock in portfolio:
            portfolio[stock] += qty
            print(f"✅ Updated {stock}: total {portfolio[stock]} shares.")
        else:
            portfolio[stock] = qty
            print(f"✅ Added {qty} shares of {stock}.")

    return portfolio


def display_portfolio(portfolio):
    print("\n" + "=" * 55)
    print("           📊 YOUR STOCK PORTFOLIO SUMMARY")
    print("=" * 55)
    print(f"{'Stock':<8} {'Qty':>6} {'Price':>12} {'Total Value':>14}")
    print("-" * 55)

    total_investment = 0
    rows = []

    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * qty
        total_investment += value
        print(f"{stock:<8} {qty:>6} ${price:>10.2f} ${value:>13.2f}")
        rows.append((stock, qty, price, value))

    print("-" * 55)
    print(f"{'TOTAL INVESTMENT':>42} ${total_investment:>13.2f}")
    print("=" * 55)

    return rows, total_investment


def save_to_file(rows, total_investment):
    save = input("\n💾 Do you want to save your portfolio to a file? (yes/no): ").lower().strip()
    if save not in ["yes", "y"]:
        return

    choice = input("Save as (1) CSV  or  (2) TXT? Enter 1 or 2: ").strip()

    if choice == "1":
        filename = "portfolio.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock Symbol", "Quantity", "Price (USD)", "Total Value (USD)"])
            for row in rows:
                writer.writerow(row)
            writer.writerow([])
            writer.writerow(["", "", "TOTAL", f"{total_investment:.2f}"])
        print(f"✅ Portfolio saved as '{filename}'")

    elif choice == "2":
        filename = "portfolio.txt"
        with open(filename, "w") as f:
            f.write("=" * 55 + "\n")
            f.write("         STOCK PORTFOLIO SUMMARY\n")
            f.write("=" * 55 + "\n")
            f.write(f"{'Stock':<8} {'Qty':>6} {'Price':>12} {'Total Value':>14}\n")
            f.write("-" * 55 + "\n")
            for stock, qty, price, value in rows:
                f.write(f"{stock:<8} {qty:>6} ${price:>10.2f} ${value:>13.2f}\n")
            f.write("-" * 55 + "\n")
            f.write(f"{'TOTAL INVESTMENT':>42} ${total_investment:>13.2f}\n")
            f.write("=" * 55 + "\n")
        print(f"✅ Portfolio saved as '{filename}'")
    else:
        print("⚠️  Invalid choice. File not saved.")


def main():
    print("=" * 55)
    print("   💹 Welcome to CodeAlpha Stock Portfolio Tracker")
    print("=" * 55)

    show_available_stocks()
    portfolio = get_portfolio()
    rows, total_investment = display_portfolio(portfolio)
    save_to_file(rows, total_investment)

    print("\nThank you for using the Stock Portfolio Tracker! 📈")


if __name__ == "__main__":
    main()
