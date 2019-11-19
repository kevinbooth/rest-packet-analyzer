"""
main.py
Main program that executes all the functions for the REST API Packet Analyzer
Created by Kevin Booth
Nov 11, 2020
"""

debug = True

from api import APIHelper
from ui import CommandLineUI

if __name__ == '__main__':
    ui = CommandLineUI()
    activity_type = ui.prompt_user()
    print(activity_type)

