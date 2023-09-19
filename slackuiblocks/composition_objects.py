from enum import StrEnum
from pydantic import BaseModel, validator
from typing import Literal


class TextType(StrEnum):
    PLAIN = "plain_text"
    MARKDOWN = "mrkdwn"


class Text(BaseModel):
    text: str

    @validator("text")
    def text_validator(cls, value: str) -> str:
        size = len(value)
        if size < 1 or size > 3000:
            raise ValueError("text should be between 1 and 3000 chars")
        return value


class PlainText(Text):
    type: Literal[TextType.PLAIN] = TextType.PLAIN
    emoji: bool = False


class MarkdownText(Text):
    type: Literal[TextType.MARKDOWN] = TextType.MARKDOWN
    verbatim: bool = False


class ConfirmStyle(StrEnum):
    PRIMARY = "primary"
    DANGER = "danger"


class ConfirmationDialog(BaseModel):
    title: PlainText
    text: PlainText
    confirm: PlainText
    deny: PlainText
    style: ConfirmStyle = ConfirmStyle.PRIMARY

    @validator("title")
    def title_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 100:
            raise ValueError("title should have less than 100 char")
        return value

    @validator("text")
    def text_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 300:
            raise ValueError("text should have less than 300 char")
        return value

    @validator("confirm")
    def confirm_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 30:
            raise ValueError("confirm should have less than 30 char")
        return value

    @validator("deny")
    def deny_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 30:
            raise ValueError("deny should have less than 30 char")
        return value


class Option(BaseModel):
    text: Text
    value: str
    description: PlainText = None
    url: str = None

    @validator("text")
    def text_validator(cls, value: Text) -> Text:
        if len(value.text) > 75:
            raise ValueError("text should be less than 75 char")
        return value

    @validator("value")
    def value_validator(cls, value: str) -> str:
        if len(value) > 75:
            raise ValueError("value should be less than 75 char")
        return value

    @validator("description")
    def description_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 75:
            raise ValueError("description should have less than 75 char")
        return value

    @validator("url")
    def url_validator(cls, value: Text) -> Text:
        if value and len(value.text) > 3000:
            raise ValueError("url should be less than 3000 char")
        return value


class OptionGroup(BaseModel):
    label: PlainText
    options: list[Option]

    @validator("label")
    def label_validator(cls, value: Text) -> Text:
        if len(value.text) > 75:
            raise ValueError("label should be less than 75 char")
        return value

    @validator("options")
    def options_validator(cls, value: list[Option]) -> list[Option]:
        if len(value) > 100:
            raise ValueError("options should have less than 100 elements")
        return value


class TriggerActions(StrEnum):
    ENTER = "on_enter_pressed"
    CHARACTER = "on_character_entered"


class DispatchActionConfig(BaseModel):
    trigger_actions_on: list[TriggerActions] = []

    @validator("trigger_actions_on")
    def trigger_actions_on_validator(
        cls, value: list[TriggerActions]
    ) -> list[TriggerActions]:
        if len(value) <= 0:
            raise ValueError("trigger actions on should have at least 1 element")
        return value


class ConversationTypes(StrEnum):
    IM = "im"
    MPIM = "mipm"
    PRIVATE = "private"
    PUBLIC = "public"


class FilterConversarionList(BaseModel):
    include: list[ConversationTypes] = []
    exclude_external_shared_channels: bool = False
    exclude_bot_users: bool = False

    @validator("include")
    def include_validator(
        cls, value: list[ConversationTypes]
    ) -> list[ConversationTypes]:
        if len(value) <= 0:
            raise ValueError("include should have at least 1 element")
        return value


class InputParameter(BaseModel):
    name: str
    value: str


class Trigger(BaseModel):
    url: str
    customizable_input_parameters: list[InputParameter] = []


class Workflow(BaseModel):
    trigger: Trigger
