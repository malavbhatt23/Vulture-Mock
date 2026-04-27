import os        # unused import
import json      # unused import
from datetime import datetime

class User:
    """Used class"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.now()

    def display(self):
        return f"{self.name} <{self.email}>"

class LegacyUser:
    """DEAD class - replaced by User"""
    def __init__(self, username):
        self.username = username

    def show(self):
        return self.username

class TempParser:
    """DEAD class - was used for a one-off migration"""
    def parse(self, data):
        return data.split(",")