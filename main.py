"""
main.py
Main program that executes all the functions for the REST API Packet Analyzer
Created by Kevin Booth
Nov 11, 2020
"""


from api import APIHelper
from ui import CommandLineUI
import json

if __name__ == '__main__':
    ui = CommandLineUI()
    api = APIHelper('https://www.boredapi.com/api/')

    # Display command line UI
    ui.welcome()
    activity_type = ui.request_activity()

    # Make API request
    response = api.get('activity?type=' + activity_type)
    data = response.json()

    #Display pretty result
    ui.display_result(data)

    # Ask to see response information
    ui.request_response_info(response)

