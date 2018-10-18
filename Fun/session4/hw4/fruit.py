prices = {
    'banana':4,
    'apple':2,
    'orange':1.5,
    'pear':3
    }
stocks = {
    'banana':6,
    'apple':0,
    'orange':32,
    'pear':15
    }
for key in stocks: # or prices
    print(key)
    print("price: ", prices[key])
    print("stock: ", stocks[key])
total = 0
value = prices[key] * stocks[key]
total += value
print(total)
# huhu lam lau qua lam xong thay minh ngu k tuong