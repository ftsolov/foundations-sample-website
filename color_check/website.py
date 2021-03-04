from flask import Flask, render_template, request
from color_check.controllers.get_color_code import get_color_code
import logging

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title="Color Check", color_hex_code='#096bd6')


@app.route('/color', methods=['POST'])
def show_color():
    # When the user submits the form at /, the contents of the form
    # will be send to this route, and whatever code you write here will
    # be run by your server. In order to render a new page for your user,
    # you will need to do a few things:
    # - extract the data submitted by the user
    # - check if the color exists in our list, return the hex code if it does
    # - render a new page which shows a square of that color and its name
    # - if the color doesn't exist, give the user a useful error message.
    # - create a log.txt file which records (logs) the user requests. 

    user_submitted_string = request.form["color"]
    joined_string = user_submitted_string.replace(" ", "")
    lowercase_string = joined_string.lower()

    # debugging
    logging.basicConfig(filename='/tmp/logs.txt', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)
    logging.debug(f"User string: {user_submitted_string}")
    print(f"User string: {user_submitted_string}")

    try:
        color_hex_code = get_color_code(lowercase_string)

    except:
        logging.error("Color not found.")
        return render_template('error.html', page_title="Error", user_color=user_submitted_string)

    user_submitted_string_capitalized = user_submitted_string.capitalize()  # capitalise first letter

    return render_template('color.html', page_title="Show Color",
                           color_hex_code=color_hex_code, color_name=user_submitted_string_capitalized)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
