#!/usr/bin/python3
"""City models - inherit from BaseModel"""
from models.base_model import BaseModel

class City(BaseModel):
    state_id: str = ""
    name: str = ""
