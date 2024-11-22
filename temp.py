# Current exchange rate from USD to CAD
exchange_rate = 1.39  # 1 USD = 1.39 CAD

# Prompt the user to enter an amount in USD
usd_amount = float(input("Enter the amount in US Dollars (USD): "))

# Convert USD to CAD
cad_amount = usd_amount * exchange_rate

# Display the result
print(f"{usd_amount} USD is equivalent to {cad_amount:.2f} CAD.")
