from pydantic import BaseModel
from enum import Enum


class ModelName(str, Enum):
    alexnet = "blah"
    resnet = "bleh"
    lenet = "bluh"



class Item(BaseModel):
    name : str
    description : str | None=None
    price : float
    tax : float

