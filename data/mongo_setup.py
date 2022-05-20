import mongoengine

def global_init():

    client = mongoengine.MongoClient(
        "mongodb+srv://<root>:<C4RI3t4HM7Pqq9T8>@cluster0.7bqpr.mongodb.net/?retryWrites=true&w=majority")
    db = client.test