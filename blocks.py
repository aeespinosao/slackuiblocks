from pydantic import BaseModel, Field, validator
from base_elements import Text

from enum import Enum

class Type:
    CONTEXT = "context"
    DIVIDER = "divider"
    FILE = "file"
    HEADER = "header"
    IMAGE = "image"


class Context(BaseModel):
    type: str = Field(Type.CONTEXT, const=True)
    elements: list[Text] # miss image
    block_id: str = None
    
    @validator('elements')
    def elements_validator(cls, value: list[Text]) -> list[Text]:
        if len(value) > 10:
            raise ValueError('elements should be less than 10 elements')
        return value
    
    @validator('block_id')
    def block_id_validator(cls, value: str) -> str:
        if len(value) > 255:
            raise ValueError('block_id should be more than 255 char')
        return value
    
    
class Divider(BaseModel):
    type: str = Field(Type.DIVIDER, const=True)
    block_id: str = None
    
    @validator('block_id')
    def block_id_validator(cls, value: str) -> str:
        if len(value) > 255:
            raise ValueError('block_id should be more than 255 char')
        return value
    

class File(BaseModel):
    type: str = Field(Type.FILE, const=True)
    external_id: str
    source: str # is constant or url= Field('remote', const=True)
    block_id: str = None
    
    @validator('block_id')
    def block_id_validator(cls, value: str) -> str:
        if len(value) > 255:
            raise ValueError('block_id should be more than 255 char')
        return value
    

class Header(BaseModel):
    type: str = Field(Type.HEADER, const=True)
    text: Text
    block_id: str = None
    
    @validator('text')
    def text_validator(cls, value: Text) -> Text:
        if len(value.text) > 150:
            raise ValueError('text should be less than 150 char')
        return value
    
    @validator('block_id')
    def block_id_validator(cls, value: str) -> str:
        if len(value) > 255:
            raise ValueError('block_id should be more than 255 char')
        return value
    

class Image(BaseModel):
    type: str = Field(Type.IMAGE, const=True)
    image_url: str
    alt_text: str
    title: Text = None
    block_id: str = None
    
    @validator('image_url')
    def image_url_validator(cls, value: str) -> str:
        if len(value) > 3000:
            raise ValueError('image_url should be less than 3000 char')
        return value
    
    @validator('image_url')
    def image_url_validator(cls, value: str) -> str:
        if len(value) > 2000:
            raise ValueError('image_url should be less than 2000 char')
        return value
    
    @validator('title')
    def title_validator(cls, value: Text) -> Text:
        if len(value.text) > 2000:
            raise ValueError('title should be less than 2000 char')
        return value
    
    @validator('block_id')
    def block_id_validator(cls, value: str) -> str:
        if len(value) > 255:
            raise ValueError('block_id should be more than 255 char')
        return value

