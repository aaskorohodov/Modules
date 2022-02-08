import pymongo
import dns

'''Можно запустить локальную базу, для это установлен софт в c/programsFiles/MongoDB
Там 2 файла:
mongod – клиент, демон, который нужно держать открытым, чтобы база работала
mongo – nерминал базы.
Файлы базы лежат на C/data
Команды:
show dbs – показать базы
show collections;  (с двоеточием с запятой)
use name – выбрать базу
db.insert({json – словарь. Лучше давать '_id':1, иначе будет присвоен автоматический id, очень сложный})

Еще есть облачная база на mongo.com, подключение к ней ниже, пароль в ссылке.
'''



client = pymongo.MongoClient("mongodb+srv://user:korn210korn@cluster0.oc6rf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
coll = db.new_users

query = {'Name': 'Vlad'}

res = db.list_collection_names()
print(res)

res = coll.count_documents({'Name': 'Vlad'})
print(res)

# res = coll.count_documents({})
# print(res)

# for v in coll.find(query, {'_id': 0, 'Name': 1}):
#     print(v)

# for v in coll.find(query):
#     print(v)

# for v in coll.find():
#     print(v)

# coll.insert_one({'_id':2, 'Name': 'Vlad222'})