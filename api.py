"""
api.py
Module to provide REST API services for a REST API
Created by Kevin Booth
Nov 11, 2020
"""

import requests


class APIHelper:
    """
    Provides functions to use a REST API
    api_full_url: string containing the full api path
        ex: 'https://www.boredapi.com/api/'
    """
    api_full_url = ''

    def __init__(self, url):
        self.api_full_url = url
        

    def get(self, resource):
        """
        Makes a GET request to the Bored API
        resource: string containing the API resource
            ex: '/activity'
        Returns: JSON Object
        """
        response = requests.get(self.api_url + resource)

        return response

