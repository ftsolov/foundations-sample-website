from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html', page_title="Home")


@app.route('/about-code')
def about_code():
    return render_template('about-code.html', page_title="About CODE")


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title="Contact")

# add additonal pages here using a similar format as above


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
