from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
posts = db['posts']
post = {
    'title': 'Hãy nói đi',
    'author': 'Pink',
    'content': 'Tháng rồi ngày sao vẫn còn ngồi nơi đây. Chờ mãi một người mơ thấy cầm tay ngại ngùng. Bật đèn hết rồi mà cứ trơ như một hòn đá...'
}
posts.insert_one(post)