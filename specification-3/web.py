from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5bbd3bef1e17016c3c5327b7814eb2e'

# Adding posts #
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
        'content': 'Making a web application using the Flask library. More information can be found on the About page',
        'date_posted': 'Nov 10, 2019'
    },

    {
        'author': 'Wojciech Bigosinski',
        'title': 'Specification 4',
        'content': 'Developing a software artefact.',
        'date_posted': 'Nov 8, 2019'
    }
]


# Homepage route #
@app.route("/")
@app.route("/home")
def home():
    """Making homepage."""
    return render_template('home.html', posts=posts)

# About page route #
@app.route("/about")
def about():
    """Making about web page."""
    return render_template('about.html', title='About')

# Specification 1 page route #
@app.route("/spec1")
def spec1():
    """Making specification 1 page."""
    return render_template('spec-1.html', title='Specification 1')


# Specification 2 page route #
@app.route("/spec2")
def spec2():
    """Making specification 2 page."""
    return render_template('spec-2.html', title='Specification 2')


# Specification 4 page route #
@app.route("/spec4")
def spec4():
    """Making specification 4 page."""
    return render_template('spec-4.html', title='Specification 4')


# Running web page and activating debugger #
if __name__ == '__main__':
    app.run(debug=True)
