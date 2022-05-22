import json, sys, os

def translate(word):
    return data(word)

try:
    print(os.path.abspath('person.json'))
    print(os.getcwd())
    data = json.load(open('person.json'))
    word = input("enter word: ")
    print(translate(word))
except Exception as e:
    print(e)