from flask_login import login_manager
from login_register import db, login_manager
from login_register import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=50), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, text_pass):
        self.password_hash = bcrypt.generate_password_hash(text_pass).decode('utf-8')

    def check_pass(self, password):
        if bcrypt.check_password_hash(self.password_hash, password):
            return True
        else:
            return False
