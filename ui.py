"""
ui.py
Module to provide classes specifically for the user interface to
connect to the Bored API
Created by Kevin Booth
Nov 18, 2020
"""

import requests


class CommandLineUI:
    """
    Provides functions to create the commandline user interface
    """
    activity_types = ['busywork', 'charity', 'cooking', 'DIY', 'education', 
                        'music', 'recreational', 'relaxation', 'social']

    def __init__(self): 
        return

    def prompt_user(self):
        """
        Prompts the user to input a type of activity they would like to try
        """

        while True:
            activity_type = input('Please select one of the nine types of activities' +
                            ' that you may be interested in.\n' +
                            '(recreational, relaxation, cooking, busywork,' +
                            ' education, social, DIY, music, and charity): ')
        
            if activity_type in self.activity_types:
                return activity_type
            else:
                print('\nYou inputted a wrong activity type.\n')
        

