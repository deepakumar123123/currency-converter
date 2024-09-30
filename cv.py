CAcd# Currency Converter Program

exchange_rates = {
    'USD': 1.0,       # Base currency
    'EUR': 0.85,      # Euro
    'GBP': 0.75,      # British Pound
    'INR': 74.0,      # Indian Rupee
    'JPY': 110.0,     # Japanese Yen
    'CAD': 1.25       # Canadian Dollar
}

def currency_converter(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency code. Please use a valid code like USD, EUR, GBP, etc."

    # Convert the amount to USD first (base currency)
    amount_in_usd = amount / exchange_rates[from_currency]
    # Convert from USD to the target currency
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    return converted_amount

def main():
    print("Welcome to Currency Converter!")
    print("Available currencies: USD, EUR, GBP, INR, JPY, CAD")

    try:
        amount = float(input("Enter the amount you want to convert: "))
        from_currency = input("Enter the currency you have (e.g., USD): ").upper()
        to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()

        converted_amount = currency_converter(amount, from_currency, to_currency)

        if isinstance(converted_amount, str):
            print(converted_amount)
        else:
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except ValueError:
        print("Invalid amount. Please enter a number.")
cd
if __name__ == "__main__":
    main()
