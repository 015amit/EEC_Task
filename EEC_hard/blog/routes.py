from flask.globals import request
from blog import app
from flask import render_template,flash,request
from blog.models import Blog
from blog import db
from datetime import datetime


app.config['SECRET_KEY'] = 'madewithheartbyagh'

@app.route('/')
def index():
    blogs = Blog.query.all()
    return render_template("home.html", blogs=blogs)

@app.route('/newblog', methods=['POST','GET'])
def newblog():
    if request.method == "POST":
        Name = request.form.get("Name")
        Email = request.form.get("email")
        Title = request.form.get("title")
        Content = request.form.get("paragraph_text")

        en = Blog(name=Name, email=Email, title=Title, content=Content, date=datetime.today().date() )
        db.session.add(en)
        db.session.commit()
        flash('Your blog is uploaded successfully')
    return render_template('newblog.html')

@app.route('/<title>')
def content(title):
    con = Blog.query.filter_by(title=title).first_or_404()
    return render_template('content.html', con=con)