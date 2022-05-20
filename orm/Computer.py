from mongoengine import Document, StringField, EmailField

class Computer(Document):
    nome = Camponome(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
