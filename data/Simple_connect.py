from mongoengine import connect
from mongoengine import Document, StringField, EmailField

connect(host="mongodb+srv://<root>:<C4RI3t4HM7Pqq9T8>@cluster0.7bqpr.mongodb.net/?retryWrites=true&w=majority"
        )


class User(Document):
    email = EmailField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


user = User(email='test@email.com')
user.first_name = 'Paris'
user.last_name = 'Nakita Kejser'
user.save()
