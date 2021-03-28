from blog import db

class Blog(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=True)
    title = db.Column(db.String(200), unique=False, nullable=False)
    content = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f'Blog {self.title}'