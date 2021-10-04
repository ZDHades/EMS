from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class equipRoom(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<>"

    def to_dict(self):
        data = {

        }

        return data


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    

    def hash_pass(self, original_password):
        self.password = generate_password_hash(original_password)

    def check_password(self, original_password):
        return check_password_hash(self.password, original_password)

    def __repr__(self):
        return f"<user: {self.email}>"

@login.user_loader
def login_user(id):
    return User.query.get(int(id))
    