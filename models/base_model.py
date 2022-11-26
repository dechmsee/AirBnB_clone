#!/usr/bin/python3
"""This is our base model"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    
    """Class from which all other classes will inherit"""
    def __init__(self, *args, **kwargs):
        """Initialises instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: list of keyword arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created at":
