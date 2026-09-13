# Python FX Converter
A Python-based foreign exchange converter with two programs for different exchage-rate use cases.

## Features
- Convert USD and TWD using bank-style buy and sell rates.
- Convert USD to multiple currencies.
- Retrieve exchange-rate data through an API.
- Process JSON data returned by the API.
- Handle user input through a command-line interface.

## Programs
### FX_Converter.py
Converts between USD and TWD using user-provided bank exchange rates.

The program supports:
- Selling USD for TWD using the bank's buy rate.
- Buying USD with TWD using the bank's sell rate.

### USD_FX_Converter.py
Converts USD into different currencies using exchange-rate data retrieved from an API.

The program demonstrates:
- Sending an HTTP GET request with "requests".
- Receiving a response from an API.
- Converting the response into Python data with .json().
- Extracting specific exchange-rate information.
- Calculating currency conversions. 

## Technologies
- Python 3
- API: https://api.exchangerate.fun/latest
- Git & GitHub

## Learning Focus
This projects was developed as part of my Python learning journey.

It demonstrates the progression from basic financial calculations to working with external APIs and structured data.

Key concepts include:
- Variables and data types
- Conditional statements
- Loops
- Funtions
- Input validation
- Python modules and packages
- HTTP requests
- JSON data processing

## Author
Zeri Wei