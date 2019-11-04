from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = '18764b774e0ce49c9ad36059879776f3'

posts = [
    {
        'author': 'Jay Mavin',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 2, 2019'
    },
    {
        'author': 'James Smith',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 3, 2019'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', Title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
