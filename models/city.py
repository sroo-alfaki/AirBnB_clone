#!/usr/bin/python3
"""City models - inherit from BaseModel"""
from models.base_model import BaseModel

class City(BaseModel):
    """City models - inherit from BaseModel"""
    state_id: str = ""
    name: str = ""
