import decimal

list_prices = []

ERROR_MSG_CANNOT_APPLY_ALGORITHM = 'Cannot apply algorithm'
ERROR_MSG_NOT_ENOUGH_PRICES = 'not enough prices!'
ERROR_MSG_ALL_PRICES_WERE_LOWEST = 'all prices are lowest!'
ERROR_MSG_ALL_PRICES_WERE_HIGHEST = 'all prices are highest!'

while True:
    value = input('Enter value: ')

    if value != 'stop':

        try:
            parsed_price = decimal.Decimal(value)
            list_prices.append(parsed_price)

        except ValueError:
            print("When I ask for a number, give me a number. Please :)")

    else:
        break

if len(list_prices) > 0:
    list_prices[:] = [price for price in list_prices if price != min(list_prices)]

    if len(list_prices) > 0:
        list_prices[:] = [price for price in list_prices if price != max(list_prices)]

        if len(list_prices) > 0:
                print(sum(list_prices)/len(list_prices))
        else:
            print(ERROR_MSG_CANNOT_APPLY_ALGORITHM + ' - ' + ERROR_MSG_ALL_PRICES_WERE_HIGHEST)
    else:
        print(ERROR_MSG_CANNOT_APPLY_ALGORITHM + ' - ' + ERROR_MSG_ALL_PRICES_WERE_LOWEST)

else:
    print(ERROR_MSG_NOT_ENOUGH_PRICES)