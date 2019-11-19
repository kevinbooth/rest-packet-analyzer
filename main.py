"""
main.py
Main program that executes all the functions for the REST API Packet Analyzer
Created by Kevin Booth
Nov 11, 2020
"""

debug = True

from api import APIHelper
from ui import CommandLineUI
import json

if __name__ == '__main__':
    ui = CommandLineUI()
    api = APIHelper('https://www.boredapi.com/api/')

    # Display command line UI
    ui.welcome()
    activity_type = ui.prompt_user()

    # Make API request
    response = api.get('activity?type=' + activity_type)

    print('\n------- API Response Information -------')
    print('Status Code: ' + str(response.status_code))
    print('Headers (JSON): \n' + json.dumps(dict(response.headers), indent=3, sort_keys=True) + '\n')
    print('Content (JSON): \n' + json.dumps(response.json(), indent=3, sort_keys=True))

