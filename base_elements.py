from enum import Enum
from pydantic import BaseModel, root_validator, validator

class TextType(Enum):
    PLAIN = "plain_text"
    MARKDOWN = "mrkdwn"

class Text(BaseModel):
    type: TextType
    text: str
    emoji: bool = False
    verbatim: bool = False
    
    @validator('text')
    def text_validator(cls, value: str) -> str:
        size = len(value)
        if size < 1 or size > 3000:
            raise ValueError('text should be between 1 and 3000 chars')
        return value
    
    @validator('emoji')
    def emoji_validator(cls, value: bool, values: dict) -> bool:
        if value and values.get('type') != TextType.PLAIN:
            raise ValueError('emoji should be use it in plain text')
        return value
        
    @validator('verbatim')
    def emoji_validator(cls, value: bool, values: dict) -> bool:
        if value and values.get('type') != TextType.MARKDOWN:
            raise ValueError('verbatim should be use it in markdown')
        return value
    

class ConfirmStyle(Enum):
    PRIMARY = "primary" 
    DANGER = "danger" 
    
class ConfirmationDialog(BaseModel):
    title: Text
    text: Text
    confirm: Text
    deny: Text
    style: ConfirmStyle = ConfirmStyle.PRIMARY
    
    @validator('title')
    def title_validator(cls, value: Text) -> Text:
        if value.type != TextType.PLAIN:
            raise ValueError('title should be plain text')
        
        if len(value.text) > 100:
            raise ValueError('title should have less than 100 char')
    
        return value

    @validator('text')
    def text_validator(cls, value: Text) -> Text:
        if value.type != TextType.PLAIN:
            raise ValueError('text should be plain text')
        
        if len(value.text) > 300:
            raise ValueError('text should have less than 300 char')
    
        return value

    @validator('confirm')
    def confirm_validator(cls, value: Text) -> Text:
        if value.type != TextType.PLAIN:
            raise ValueError('confirm should be plain text')
        
        if len(value.text) > 30:
            raise ValueError('confirm should have less than 30 char')
    
        return value
    
    @validator('deny')
    def deny_validator(cls, value: Text) -> Text:
        if value.type != TextType.PLAIN:
            raise ValueError('deny should be plain text')
        
        if len(value.text) > 30:
            raise ValueError('deny should have less than 30 char')
    
        return value
    
    
class Option(BaseModel):
    text: Text
    value: str
    description: Text = None
    url: str = None
    
    @validator('text')
    def text_validator(cls, value: Text) -> Text:
        if len(value.text) > 75:
            raise ValueError('text should have less than 75 char')
        return value
    
    @validator('value')
    def value_validator(cls, value: Text) -> Text:
        if len(value) > 75:
            raise ValueError('value should have less than 75 char')
        return value
    
    @validator('description')
    def description_validator(cls, value: Text) -> Text:
        if value and len(value.text) > 75:
            raise ValueError('description should have less than 75 char')
        return value
    
    @validator('url')
    def url_validator(cls, value: Text) -> Text:
        if value and len(value.text) > 3000:
            raise ValueError('url should have less than 3000 char')
        return value
    
class OptionGroup(BaseModel):
    label: Text
    options: list[Option]
    
    @validator('label')
    def label_validator(cls, value: Text) -> Text:
        if value.type != TextType.PLAIN:
            raise ValueError('label should be plain text')
        
        if len(value.text) > 75:
            raise ValueError('label should have less than 75 char')
        return value
    
    @validator('options')
    def options_validator(cls, value: list[Option]) -> list[Option]:
        if len(value) > 100:
            raise ValueError('options should have less than 100 elements')
        return value