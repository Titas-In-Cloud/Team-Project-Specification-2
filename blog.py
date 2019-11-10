from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5bbd3bef1e17016c3c5327b7814eb2e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}'"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Lapshun Chung',
        'title': 'Specification 1',
        'content': 'Exploring frequency analysis of large text files and producing a visual way of analysis results. '
        ,
        'date_posted': 'Nov 12, 2019'
    },
    {
        'author': 'Titas Petelis',
        'title': 'Specification 2',
        'content': 'Exploring image manipulation using the Pillow Python library.',
        'date_posted': 'Nov 11, 2019'
    },
    {
        'author': 'Jay Mavin',
        'title': 'Specification 3',
        'content': 'Making a web application using the Flask library. This can be found in the Home page',
        'date_posted': 'Nov 10, 2019'
    },

    {
        'author': 'Wojciech Bigosinski',
        'title': 'Specification 4',
        'content': 'Developing a software artefact.',
        'date_posted': 'Nov 8, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'jaymavin123@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/spec1")
def spec1():
    return render_template('spec-1.html', title='Specification 1')


@app.route("/spec2")
def spec2():
    return render_template('spec-2.html', title='Specification 2')


@app.route("/spec3")
def spec3():
    return render_template('spec-3.html', title='Specification 3')


@app.route("/spec4")
def spec4():
    return render_template('spec-4.html', title='Specification 4')


if __name__ == '__main__':
    app.run(debug=True)
