# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.

import json
import os
import logging


def get_color_code(color_name):
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.

    # open json file and store
    with open('color_check/data/css-color-names.json', 'r') as color_database:
        data_dict = json.load(color_database)

        if color_name in data_dict:
            hex_code = data_dict[color_name]  # get hex code
            logging.debug(f"Hex code is: {hex_code}")
            return hex_code
        else:
            raise Exception("Color not found, please try again.")