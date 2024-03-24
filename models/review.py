#!/usr/bin/python3
"""Review class - inherits from BaseModel."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class - inherits from BaseModel."""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
