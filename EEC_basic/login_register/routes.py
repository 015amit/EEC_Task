from flask import render_template,redirect,url_for, flash
from login_register import app
from login_register.form import RegisterForm, LoginForm
from login_register.models import User
from login_register import db
from flask_login import login_user

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        create = User(name=form.name.data,
                              email=form.email.data,
                              password=form.password1.data)
        db.session.add(create)
        db.session.commit()
        return redirect(url_for('home'))
    if form.errors != {}:
        for error in form.errors.values():
            flash(error)
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_pass(password=form.password.data):
            login_user(user)
            flash(f'{user.name} are logged in !')
            return render_template('after_login.html')
        else:
            flash('Incorrect username or password')
    return render_template('login.html', form=form)