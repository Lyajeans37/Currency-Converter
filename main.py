
#### `main.py`
```python
import requests

def get_exchange_rate(from_currency, to_currency):
    api_key = "your_api_key"  # Replace with your actual API key
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        rates = response.json()["rates"]
        return rates.get(to_currency, None)
    else:
        return None

def main():
    from_currency = input("Enter the base currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    if exchange_rate:
        converted_amount = amount * exchange_rate
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Failed to get the exchange rate.")

if __name__ == "__main__":
    main()
