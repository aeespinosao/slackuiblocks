from pydantic import BaseModel, validator
from .composition_objects import Text, PlainText
from .block_elements import BlockElement, Image, InputElement, SectionElement

from enum import StrEnum
from typing import Literal


class Type(StrEnum):
    ACTIONS = "actions"
    CONTEXT = "context"
    DIVIDER = "divider"
    FILE = "file"
    HEADER = "header"
    IMAGE = "image"
    INPUT = "input"
    SECTION = "section"
    VIDEO = "video"


class LayoutBlock(BaseModel):
    block_id: str = None

    class Config:
        arbitrary_types_allowed = True

    @validator("block_id")
    def block_id_validator(cls, value: str) -> str:
        if len(value) > 255:
            raise ValueError("block_id should be less than 255 char")
        return value


class Actions(LayoutBlock):
    type: Literal[Type.ACTIONS] = Type.ACTIONS
    elements: list[BlockElement]

    @validator("elements")
    def elements_validator(cls, value: list[BlockElement]) -> list[BlockElement]:
        if len(value) > 25:
            raise ValueError("elements should be less than 25 elements")
        return value


class Context(LayoutBlock):
    type: Literal[Type.CONTEXT] = Type.CONTEXT
    elements: list[Text | Image]

    @validator("elements")
    def elements_validator(cls, value: list[Text | Image]) -> list[Text | Image]:
        if len(value) > 10:
            raise ValueError("elements should be less than 10 elements")
        return value


class Divider(LayoutBlock):
    type: Literal[Type.DIVIDER] = Type.DIVIDER


class File(LayoutBlock):
    type: Literal[Type.FILE] = Type.FILE
    source: str = Literal["remote"]
    external_id: str


class Header(LayoutBlock):
    type: Literal[Type.HEADER] = Type.HEADER
    text: PlainText

    @validator("text")
    def text_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 150:
            raise ValueError("text should be less than 150 char")
        return value


class Image(LayoutBlock):
    type: Literal[Type.IMAGE] = Type.IMAGE
    image_url: str
    alt_text: str
    title: PlainText = None

    @validator("image_url")
    def image_url_validator(cls, value: str) -> str:
        if len(value) > 3000:
            raise ValueError("image_url should be less than 3000 char")
        return value

    @validator("alt_text")
    def alt_text_validator(cls, value: str) -> str:
        if len(value) > 2000:
            raise ValueError("alt_text should be less than 2000 char")
        return value

    @validator("title")
    def title_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 2000:
            raise ValueError("title should be less than 2000 char")
        return value


class Input(LayoutBlock):
    type: Literal[Type.INPUT] = Type.INPUT
    label: PlainText
    element: InputElement
    dispatch_action: bool = False

    hint: PlainText = None
    optional: bool = False

    @validator("label")
    def label_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 2000:
            raise ValueError("label should be less than 2000 char")
        return value

    @validator("hint")
    def hint_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 2000:
            raise ValueError("hint should be less than 2000 char")
        return value


class Section(LayoutBlock):
    type: Literal[Type.SECTION] = Type.SECTION
    text: Text = None
    fields: list[Text] = None
    accessory: SectionElement = None

    @validator("text")
    def text_validator(cls, value: Text, values: dict) -> Text:
        fields = values.get("fields")
        if value is None:
            if fields is None:
                raise ValueError("text or fields is required")
            elif len(fields) == 0:
                raise ValueError("text or fields is required")

        size = len(value.text)
        if size > 3000 or size < 1:
            raise ValueError("text should be between 1 and 3000 char")
        return value

    @validator("fields")
    def fields_validator(cls, value: list[Text], values: dict) -> Text:
        text = values.get("text")
        if value is None and text is None:
            raise ValueError("text or fields is required")
        if len(value) == 0 and text is None:
            raise ValueError("text or fields is required")

        for element in value:
            size = len(element.text)
            if size > 3000 or size < 1:
                raise ValueError("text should be between 1 and 3000 char")
        return value


class Video(LayoutBlock):
    type: Literal[Type.VIDEO] = Type.VIDEO
    alt_text: str
    author_name: str = None
    description: PlainText = None
    provider_icon_url: str = None
    provider_name: str = None
    title: PlainText
    title_url: str = None
    thumbnail_url: str
    video_url: str

    @validator("author_name")
    def author_name_validator(cls, value: str) -> str:
        if len(value) > 50:
            raise ValueError("author_name should be less than 50 char")
        return value

    @validator("title")
    def title_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 200:
            raise ValueError("title should be less than 200 char")
        return value
