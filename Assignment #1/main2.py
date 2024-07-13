#   EMAN FURRUKH    #
#     21I-1726      #
#   ASSIGNMENT 1b   #

                            #   QUESTION 5  #
import requests
date = str(input("Enter date to convert from: "))
fromCurrency = str(input("Enter currency from: ")).upper()        #enter in caps
toCurrency = str(input("Enter currency to: ")).upper()            #enter in caps
amount = float(input("Enter the amount: "))
conversion = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
print("Conversion on ",date," is: ") 
print(
    f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
