import pymongo

conn = pymongo.MongoClient(
            host='localhost',
            port=27017,
            # authSource='admin',
            # authMechanism='SCRAM-SHA-256',
            username='admin',
            password='password'
        )
db = conn['quotes_db']
collection = db['quotes']
collection.insert_one({"name": "test"})
