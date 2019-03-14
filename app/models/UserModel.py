from . import db
from . import ma
import logging


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, data):
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.age = data.get('age')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_users():
        users = UserModel.query.all()
        return users_schema.dump(users).data

    @staticmethod
    def get_user(id):
        user = UserModel.query.get(id)
        return user_schema.dump(user).data


class UserSchema(ma.TableSchema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'age')


user_schema = UserSchema()
users_schema = UserSchema(many=True, strict=True)
