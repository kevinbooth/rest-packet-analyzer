"""
ui.py
Module to provide classes specifically for the user interface to
connect to the Bored API
Created by Kevin Booth
Nov 18, 2020
"""

import requests
import json

class CommandLineUI:
    """
    Provides functions to create the command line user interface
    """
    activity_types = ['busywork', 'charity', 'cooking', 'diy', 'education', 
                        'music', 'recreational', 'relaxation', 'social']

    def __init__(self): 
        return

    def welcome(self):
        """
        Prints the welcome message
        Returns: void
        """
        print('Welcome to the REST API Packet Analyzer\n' +
              'Courtesy of The Bored REST API\n' +
              '---------------------------------------\n')

    def request_activity(self):
        """
        Prompts the user to input a type of activity they would like to try
        Returns: void
        """
        while True:
            activity_type = input('Please select one of the nine types of \n' +
                                  'activities that you may be interested \n' +
                                  'in. (recreational, relaxation, cooking, \n' +
                                  'busywork, education, social, DIY, \n' +
                                  'music, and charity): ')
        
            if activity_type.lower() in self.activity_types:
                return activity_type
            else:
                print('\nYou inputted a wrong activity type.\n')

    def request_response_info(self, response):
        """
        Prompts the user if they would like to see API response information
        Returns: void
        """
        while True:
            answer = input('\nWould you like to see the developer \n' +
                           'information regarding the API request? \n' +
                           '[Y/N]: ')
            
            if answer in ['Y', 'y', 'yes', 'N', 'n', 'no']:
                self.display_response_info(response)
                return
            else:
                print('\nYou inputted a wrong activity type.\n')

    def display_result(self, activity):
        """
        Displays activity results
        Returns: void
        """
        print('\n-------- Here\'s Your Activity --------\n' + activity['activity'])
        print('  Participants Needed:', activity['participants'])
        print('  Price (0-1 [0-$$$]):', activity['price'])
        print('  Accessibility (0-1 [easy-hard]):', activity['price'])

    def display_response_info(self, response):
        """
        Displays API response information
        Returns: void
        """
        print('\n--- API Packet Response Information ----')
        print('Status Code:', str(response.status_code))
        print('Response History Status Codes:', str(response.history))
        print('Server URL Requested:', str(response.url))
        print('Packet Size (bytes):', str(len(response.content)))
        print('Headers (JSON): \n' + json.dumps(dict(response.headers), indent=3, sort_keys=True) + '\n')
        print('Content (JSON): \n' + json.dumps(response.json(), indent=3, sort_keys=True))
        

