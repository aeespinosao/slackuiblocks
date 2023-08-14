from pydantic import BaseModel, Field, validator
from composition_objects import Text
from block_elements import BlockElement

from enum import Enum

class Type:
    ACTIONS = "actions"
    CONTEXT = "context"
    DIVIDER = "divider"
    FILE = "file"
    HEADER = "header"
    IMAGE = "image"
    INPUT = "input"
    SECTION = "section"


class Actions(BaseModel):
    type: str = Field(Type.ACTIONS, const=True)
    elements: list[BlockElement]
    block_id: str = None
    
    @validator('elements')
    def elements_validator(cls, value: list[Text]) -> list[Text]:
        if len(value) > 25:
            raise ValueError('elements should be less than 25 elements')
        return value
    
class Context(BaseModel):
    type: str = Field(Type.CONTEXT, const=True)
    elements: list[Text] # TODO: include image
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


class Input(BaseModel):
    type: str = Field(Type.INPUT, const=True)
    label: str
    element: Text # TODO: include checkbox, radio, select, multiselect, datepicker
    dispatch_action: bool = False
    block_id: str = None
    hint: Text = None
    optional: bool = False

    @validator('block_id')
    def block_id_validator(cls, value: str) -> str:
        if len(value) > 255:
            raise ValueError('block_id should be more than 255 char')
        return value
    
    @validator('hint')
    def hint_validator(cls, value: Text) -> Text:
        if len(value.text) > 2000:
            raise ValueError('hint should be less than 2000 char')
        return value
    

class Section(BaseModel):
    type: str = Field(Type.SECTION, const=True)
    text: Text = None
    block_id: str = None
    fields: list[Text] = None
    accessory: dict = None # TODO: need elements objects
    
    """@validator('text')
    def text_validator(cls, value: Text, values: dict) -> Text:
        if value and len(values.get('fields')) == 0:
            size = len(value.text)
            if size > 3000 or size < 1:
                raise ValueError('text should be between 1 and 3000 char')
        return value
    
    @validator('block_id')
    def block_id_validator(cls, value: str) -> str:
        if value and len(value) > 255:
            raise ValueError('block_id should be less than 255 char')
        return value
    
    @validator('fields')
    def fields_validator(cls, value: list[Text], values: dict) -> Text:
        if values.get('text') is None:
            size = len(value)
            if value and (size < 1 or size > 10):
                raise ValueError('fields should be less than 10 elements')
            
            for element in value:
                if len(element.text) > 2000:
                    raise ValueError('all elements in fields should be less than than 2000 char')
                    
        return value"""
        
    
class Video(BaseModel):
    alt_text: str
    author_name: str = None
    block_id: str = None
    description: Text = None
    provider_icon_url: str = None
    provider_name: str = None
    title: Text
    title_url: str = None
    thumbnail_url: str
    video_url: str
    
    @validator('author_name')
    def author_name_validator(cls, value: str) -> str:
        if len(value) > 50:
            raise ValueError('author_name should be less than 50 char')
        return value
    
    @validator('block_id')
    def block_id_validator(cls, value: str) -> str:
        if len(value) > 255:
            raise ValueError('block_id should be more than 255 char')
        return value
    
    @validator('title')
    def title_validator(cls, value: str) -> str:
        if len(value) > 200:
            raise ValueError('title should be less than 200 char')
        return value