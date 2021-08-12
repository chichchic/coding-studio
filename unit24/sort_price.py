def sort_price(price_info):
    price_info = list(map(int, price_info.split(';')))
    price_info.sort()
    price_info.reverse()
    return price_info


input_price = input()
for price in sort_price(input_price):
    print('%9s' % format(price, ','))
