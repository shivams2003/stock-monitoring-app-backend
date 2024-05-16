# api/models.py
import mongoengine as me

class User(me.Document):
    username = me.StringField(required=True, max_length=100)
    email = me.EmailField(required=True, unique=True)
    password = me.StringField(required=True)
    meta = {'collection': 'users'}

class Watchlist(me.Document):
    user_id = me.ReferenceField(User, required=True)
    stocks = me.ListField(me.StringField(max_length=10))
    meta = {'collection': 'watchlists'}
