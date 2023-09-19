from .layout_blocks import LayoutBlock
from pydantic import BaseModel, validator
from .composition_objects import PlainText


from enum import StrEnum
from typing import Literal


class Type(StrEnum):
    MODAL = "modal"
    HOME = "home"


from typing import List


class Views(BaseModel):
    blocks: List[LayoutBlock] = []

    class Config:
        arbitrary_types_allowed = True

    @validator("blocks")
    def blocks_validator(cls, value: list[LayoutBlock]) -> list[LayoutBlock]:
        if len(value) > 100:
            raise ValueError("blocks should be less than 100")
        return value


class Blocks(Views):
    def to_dict(self):
        return self.model_dump(exclude_none=True).get("blocks")


class ModalView(Views):
    type: Literal[Type.MODAL] = Type.MODAL
    title: PlainText
    blocks: list[LayoutBlock]
    close: PlainText = None
    submit: PlainText = None
    private_metadata: str = None
    callback_id: str = None
    clear_on_close: bool = False
    notify_on_close: bool = False
    external_id: str = None
    submit_disabled: bool = False

    @validator("title")
    def title_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 24:
            raise ValueError("title should be less than 24 char")
        return value

    @validator("close")
    def close_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 24:
            raise ValueError("title should be less than 24 char")
        return value

    @validator("submit")
    def submit_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 24:
            raise ValueError("title should be less than 24 char")
        return value

    @validator("private_metadata")
    def private_metadata_validator(cls, value: str) -> str:
        if len(value) > 3000:
            raise ValueError("private metadata should be less than 3000 char")
        return value

    @validator("callback_id")
    def callback_id_validator(cls, value: str) -> str:
        if len(value) > 255:
            raise ValueError("callback id should be less than 255 char")
        return value

    def to_dict(self):
        return self.dict(exclude_none=True)


class HomeView(Views):
    type: Literal[Type.HOME] = Type.HOME
    blocks: list[LayoutBlock]
    private_metadata: str = None
    callback_id: str = None
    external_id: str = None

    @validator("private_metadata")
    def private_metadata_validator(cls, value: str) -> str:
        if len(value) > 3000:
            raise ValueError("private metadata should be less than 3000 char")
        return value

    @validator("callback_id")
    def callback_id_validator(cls, value: str) -> str:
        if len(value) > 255:
            raise ValueError("callback id should be less than 255 char")
        return value

    def to_dict(self):
        return self.dict(exclude_none=True)
