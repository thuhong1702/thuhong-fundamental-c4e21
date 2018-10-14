from pymongo import MongoClient

uri = "mongodb://hongthu:hong012356789@ds245022.mlab.com:45022/databasec4e"

# connect to database
client = MongoClient(uri)
db = client.get_default_database()

# collection
posts = db['Posts']

# document

# create a document
# post = {
#     'title': 'thefallenn',
#     'content': 'fuckboy',
#     'author': 'me'
# }

# insert create document insert_one (C)), find (R)
# posts.insert_one(post)
post_list = posts.find()
for p in post_list:
    
    # p = post_list[0]
    print(p['title'])
    print(p['author'])
