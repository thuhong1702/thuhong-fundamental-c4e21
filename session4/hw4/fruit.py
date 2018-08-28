prices= {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

stocks= {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
for key in prices:
    
    print "prices: %s" % prices[key]
    print "stocks: %s" % stocks[key]
total = 0
for key in prices:
    print prices[key] * stocks[key]
    total = total + prices[key] * stocks[key]
print total