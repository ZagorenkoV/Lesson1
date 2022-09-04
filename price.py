def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    delimiter = str('&')
    return str(one + delimiter + two)
summ = get_summ("Learn", "python").upper()
print(summ)

def format_price(price):
    price = int(price)
    return f"Цена: {price} руб."

final_price = format_price(56.24)
print(final_price)