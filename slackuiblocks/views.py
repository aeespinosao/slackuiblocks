from layout_blocks import LayoutBlock
from pydantic import BaseModel, Field
from .composition_objects import PlainText


from enum import StrEnum


class Type(StrEnum):
    MODAL = "modal"
    HOME = "home"


class Blocks(BaseModel):
    blocks: list[LayoutBlock] = []


class ModalView(BaseModel):
    type: Type = Field(Type.MODAL, const=True)
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


class HomeView(BaseModel):
    type: Type = Field(Type.HOME, const=True)
    blocks: list[LayoutBlock]
    private_metadata: str = None
    callback_id: str = None
    external_id: str = None
