from pymongo import MongoClient
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
customers = db['customers']

events = customers.find({'ref':'events'}).count()
woms = customers.find({'ref'})
ads = ...

# ghep thanh list

# pyplot.pie(customers_count, labels= customers_ref, autopct="%.1%%")
# pyplot.title("in4customer")
# pyplot.axis("equal")
# pyplot.show()
   