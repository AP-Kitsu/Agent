from mongoengine import connect
from mongoengine.errors import NotUniqueError
from orm.user import User

connect(host="mongodb+srv://AgentUsr:Logiologio1998@cluster0.7bqpr.mongodb.net/?retryWrites=true&w=majority")

try:
    user = User(email='test@email.com')
    user.first_name = 'Paris'
    user.last_name = 'Nakita Kejser'
    user.save()
except NotUniqueError as e:
    print('E-mail allready found')