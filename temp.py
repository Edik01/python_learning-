

amount = float(input("Hi! enter the amount in USD:"))
currency = input("Enter the target currency (e.g., EUR, CAD, GBP): ").upper()
try:
    exchange_rate = c.get_rate('USD', currency)
    converted_amount = c.convert('USD', currency, amount)
    print(f"The exchange rate from USD to {currency} is {exchange_rate:.2f}")
    print(f"{amount} USD is equivalent to {converted_amount:.2f} {currency}.")
except Exception as e:
    print(f"An error occurred: {e}")


# Current exchange rate from USD to CAD
exchange_rate = 1.39  # 1 USD = 1.39 CAD

# Prompt the user to enter an amount in USD
usd_amount = float(input("Enter the amount in US Dollars (USD): "))

# Convert USD to CAD
cad_amount = usd_amount * exchange_rate

# Display the result
print(f"{usd_amount} USD is equivalent to {cad_amount:.2f} CAD.")


