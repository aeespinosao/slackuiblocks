from pydantic import BaseModel, validator
from .composition_objects import (
    Text,
    PlainText,
    ConfirmationDialog,
    Option,
    DispatchActionConfig,
    OptionGroup,
    FilterConversarionList,
    Workflow,
)
from enum import StrEnum
from abc import ABC
from typing import Literal


class ElementType(StrEnum):
    BUTTON = "button"
    CHECKBOXES = "checkboxes"
    DATEPICKER = "datepicker"
    DATETIMEPICKER = "datetimepicker"
    EMAILINPUT = "email_text_input"
    IMAGE = "image"
    MULTISELECTSTATIC = "multi_static_select"
    MULTISELECTEXTERNALDATA = "multi_external_select"
    MULTISELECTUSERLIST = "multi_users_select"
    MULTISELECTCONVERSATIONLIST = "multi_conversations_select"
    MULTISELECTCHANNELSLIST = "multi_channels_select"
    NUMBERINPUT = "number_input"
    OVERFLOWMENU = "overflow"
    TEXTINPUT = "plain_text_input"
    RADIOBUTTON = "radio_buttons"
    SELECTSTATIC = "static_select"
    SELECTEXTERNALDATA = "external_select"
    SELECTUSER = "users_select"
    SELECTCONVERSATION = "conversations_select"
    SELECTPUBLICCHANNEL = "channels_select"
    TIMEPICKER = "timepicker"
    URLINPUT = "url_text_input"
    WORKFLOWBUTTON = "workflow_button"


class Style(StrEnum):
    PRIMARY = "primary"
    DANGER = "danger"


class BlockElement(BaseModel):
    action_id: str = None

    @validator("action_id")
    def action_id_validator(cls, value: str) -> str:
        if len(value) > 255:
            raise ValueError("action_id should be less than 75 char")
        return value


class SectionElement(ABC):
    pass


class ActionElement(ABC):
    pass


class InputElement(ABC):
    pass


class Button(BlockElement, SectionElement, ActionElement):
    type: Literal[ElementType.BUTTON] = ElementType.BUTTON
    text: PlainText
    url: str = None
    value: str = None
    style: Style = None  # TODO: no send when is default
    confirm: ConfirmationDialog = None
    accessibility_label: Text = None

    @validator("text")
    def text_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 75:
            raise ValueError("text should be less than 75 char")
        return value

    @validator("url")
    def url_validator(cls, value: str) -> str:
        if len(value) > 3000:
            raise ValueError("url should be less than 3000 char")
        return value

    @validator("value")
    def value_validator(cls, value: str) -> str:
        if len(value) > 2000:
            raise ValueError("value should be less than 2000 char")
        return value

    @validator("accessibility_label")
    def accessibility_label_validator(cls, value: Text) -> Text:
        if len(value.text) > 75:
            raise ValueError("accessibility label should be less than 75 char")
        return value


class CheckboxGroups(BlockElement, SectionElement, ActionElement, InputElement):
    type: Literal[ElementType.CHECKBOXES] = ElementType.CHECKBOXES
    options: list[Option]
    initial_options: list[Option] = None
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False

    @validator("options")
    def options_validator(cls, value: list[Option]) -> list[Option]:
        if len(value) > 10:
            raise ValueError("options should be less than 10 elements")
        return value

    @validator("initial_options")
    def initial_options_validator(cls, value: list[Option]) -> list[Option]:
        # TODO: implement validations, should be in options object
        return value


class Datepicker(BlockElement, SectionElement, ActionElement, InputElement):
    type: Literal[ElementType.DATEPICKER] = ElementType.DATEPICKER
    initial_date: str = None
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False
    placeholder: PlainText = None

    @validator("placeholder")
    def placeholder_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 150:
            raise ValueError("placeholder should be less than 150 char")
        return value

    @validator("initial_date")
    def initial_date_validator(cls, value: str) -> str:
        # TODO: validate YYYY-MM-DD format
        return value


class Datetimepicker(BlockElement, ActionElement, InputElement):
    type: Literal[ElementType.DATETIMEPICKER] = ElementType.DATETIMEPICKER
    initial_date_time: int = None
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False

    @validator("initial_date_time")
    def initial_date_time_validator(cls, value: int) -> int:
        from datetime import datetime

        if len(str(value)) != 10:
            raise ValueError("initial date time should have 10 char")
        try:
            _ = datetime.fromtimestamp(value)
        except Exception:
            raise ValueError("initial date time in bad format")
        return value


class EmailInput(BlockElement, InputElement):
    type: Literal[ElementType.EMAILINPUT] = ElementType.EMAILINPUT
    initial_value: str = None
    dispatch_action_config: DispatchActionConfig = None
    focus_on_load: bool = False
    placeholder: PlainText = None

    @validator("placeholder")
    def placeholder_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 150:
            raise ValueError("placeholder should be less than 150 char")
        return value


class Image(BlockElement, SectionElement):
    type: Literal[ElementType.IMAGE] = ElementType.IMAGE
    action_id: str = Literal[None]
    image_url: str
    alt_text: str


class Multiselect(BlockElement, SectionElement, InputElement):
    confirm: ConfirmationDialog = None
    max_selected_items: int = 1
    focus_on_load: bool = False
    placeholder: PlainText = None

    @validator("max_selected_items")
    def max_selected_items_validator(cls, value: int) -> int:
        if value < 1:
            raise ValueError("max selected items should be more than 1")
        return value

    @validator("placeholder")
    def placeholder_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 150:
            raise ValueError("placeholder should be less than 150 char")
        return value


class MultiselectStatic(Multiselect):
    type: Literal[ElementType.MULTISELECTSTATIC] = ElementType.MULTISELECTSTATIC
    options: list[Option] = None
    option_groups: list[OptionGroup] = None
    initial_options: list[Option] = None

    @validator("options")
    def options_validator(cls, value: list[Option], values: dict) -> list[Option]:
        groups = values.get("option_groups")
        if value is None and groups is None:
            raise ValueError("should have attribute options or options groups")

        if groups is None:
            if len(value) > 100:
                raise ValueError("options should be less than 100 elements")

            for option in value:
                if len(option.text.text) > 76:
                    raise ValueError("each option should have less than 76 char")
        return value

    @validator("option_groups")
    def option_groups_validator(
        cls, value: list[OptionGroup], values: dict
    ) -> list[OptionGroup]:
        options = values.get("option_groups")
        if value is None and options is None:
            raise ValueError("should have attribute options or options groups")

        if options is None:
            if len(value) > 100:
                raise ValueError("options should be less than 100 elements")
        return value

    @validator("initial_options")
    def initial_options_validator(cls, value: list[Option]) -> list[Option]:
        # TODO: implement validations, should be in options object or options groups
        return value


class MultiselectExternalData(Multiselect):
    type: Literal[
        ElementType.MULTISELECTEXTERNALDATA
    ] = ElementType.MULTISELECTEXTERNALDATA
    min_query_length: int = 3
    initial_options: list[Option] = None

    @validator("min_query_length")
    def min_query_length_validator(cls, value: int) -> int:
        if value < 1:
            raise ValueError("min query lenght should be more than 1")
        return value

    @validator("initial_options")
    def initial_options_validator(cls, value: list[Option]) -> list[Option]:
        # TODO: implement validations, should be in options object or options groups
        return value


class MultiselectUserList(Multiselect):
    type: Literal[ElementType.MULTISELECTUSERLIST] = ElementType.MULTISELECTUSERLIST
    initial_users: list[str] = None


class MultiselectConversationList(Multiselect):
    type: Literal[
        ElementType.MULTISELECTCONVERSATIONLIST
    ] = ElementType.MULTISELECTCONVERSATIONLIST
    initial_conversations: list[str] = None
    default_to_current_conversation: bool = False
    filter: FilterConversarionList = None


class MultiselectPublicChannels(Multiselect):
    type: Literal[
        ElementType.MULTISELECTCHANNELSLIST
    ] = ElementType.MULTISELECTCHANNELSLIST
    initial_channels: list[str] = None


class NumberInput(BlockElement, InputElement):
    type: Literal[ElementType.NUMBERINPUT] = ElementType.NUMBERINPUT
    is_decimal_allowed: bool
    initial_value: str = None
    min_value: str = None
    max_value: str = None
    dispatch_action_config: DispatchActionConfig = None
    focus_on_load: bool = False
    placeholder: PlainText = None

    @validator("placeholder")
    def placeholder_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 150:
            raise ValueError("placeholder should be less than 150 char")
        return value


class OverflowMenu(BlockElement, SectionElement, ActionElement):
    type: Literal[ElementType.OVERFLOWMENU] = ElementType.OVERFLOWMENU
    options: list[Option]
    confirm: ConfirmationDialog = None

    @validator("options")
    def options_validator(cls, value: list[Option]) -> list[Option]:
        if len(value) > 5:
            raise ValueError("options should be less than 5 elements")
        return value


class PlainTextInput(BlockElement, InputElement):
    type: Literal[ElementType.TEXTINPUT] = ElementType.TEXTINPUT
    initial_value: str = None
    multiline: bool = False
    min_length: int = None
    max_length: int = None
    dispatch_action_config: DispatchActionConfig = None
    focus_on_load: bool = False
    placeholder: PlainText = None

    @validator("min_length")
    def min_length_validator(cls, value: int) -> int:
        if value > 3000:
            raise ValueError("min length should be less than 3000")
        return value


class RadioButton(BlockElement, SectionElement, ActionElement, InputElement):
    type: Literal[ElementType.RADIOBUTTON] = ElementType.RADIOBUTTON
    options: list[Option]
    initial_option: list[Option] = None
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False

    @validator("options")
    def options_validator(cls, value: list[Option]) -> list[Option]:
        if len(value) > 10:
            raise ValueError("options should be less than 10 elements")
        return value

    @validator("initial_option")
    def initial_options_validator(cls, value: list[Option]) -> list[Option]:
        # TODO: implement validations, should be in options object or options groups
        return value


class SelectMenu(BlockElement, SectionElement, ActionElement, InputElement):
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False
    placeholder: PlainText = None


class SelectStatic(SelectMenu):
    type: Literal[ElementType.SELECTSTATIC] = ElementType.SELECTSTATIC
    options: list[Option]
    option_groups: list[OptionGroup] = None
    initial_option: Option = None

    @validator("options")
    def options_validator(cls, value: list[Option], values: dict) -> list[Option]:
        groups = values.get("option_groups")
        if value is None and groups is None:
            raise ValueError("should have attribute options or options groups")

        if groups is None:
            if len(value) > 100:
                raise ValueError("options should be less than 100 elements")

            for option in value:
                if len(option.text.text) > 76:
                    raise ValueError("each option should have less than 76 char")
        return value

    @validator("option_groups")
    def option_groups_validator(
        cls, value: list[OptionGroup], values: dict
    ) -> list[OptionGroup]:
        options = values.get("option_groups")
        if value is None and options is None:
            raise ValueError("should have attribute options or options groups")

        if options is None:
            if len(value) > 100:
                raise ValueError("options should be less than 100 elements")
        return value

    @validator("initial_option")
    def initial_option_validator(cls, value: list[Option]) -> list[Option]:
        # TODO: implement validations, should be in options object or options groups
        return value


class SelectExternalData(SelectMenu):
    type: Literal[ElementType.SELECTEXTERNALDATA] = ElementType.SELECTEXTERNALDATA
    initial_option: Option = None
    min_query_length: int = 3

    @validator("min_query_length")
    def min_query_length_validator(cls, value: int) -> int:
        if value < 1:
            raise ValueError("min query lenght should be more than 1")
        return value

    @validator("initial_option")
    def initial_option_validator(cls, value: list[Option]) -> list[Option]:
        # TODO: implement validations, should be in options object or options groups
        return value


class SelectUser(SelectMenu):
    type: Literal[ElementType.SELECTUSER] = ElementType.SELECTUSER
    initial_user: str = None


class SelectConversation(SelectMenu):
    type: Literal[ElementType.SELECTCONVERSATION] = ElementType.SELECTCONVERSATION
    initial_conversation: str = None
    default_to_current_conversation: bool = False
    response_url_enabled: bool = False
    filter: FilterConversarionList = None


class SelectPublicChannel(SelectMenu):
    type: Literal[ElementType.SELECTPUBLICCHANNEL] = ElementType.SELECTPUBLICCHANNEL
    initial_channel: str = None
    response_url_enabled: bool = False


class TimePicker(BlockElement, SectionElement, ActionElement, InputElement):
    type: Literal[ElementType.TIMEPICKER] = ElementType.TIMEPICKER
    initial_time: str = None
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False
    placeholder: PlainText = None
    timezone: str = None

    @validator("placeholder")
    def placeholder_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 150:
            raise ValueError("placeholder should be less than 150 char")
        return value


class UrlInput(BlockElement, InputElement):
    type: Literal[ElementType.URLINPUT] = ElementType.URLINPUT
    initial_value: str = None
    dispatch_action_config: DispatchActionConfig = None
    focus_on_load: bool = False
    placeholder: PlainText = None

    @validator("placeholder")
    def placeholder_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 150:
            raise ValueError("placeholder should be less than 150 char")
        return value


class WorkflowButton(BlockElement, SectionElement, ActionElement):
    type: Literal[ElementType.WORKFLOWBUTTON] = ElementType.WORKFLOWBUTTON
    text: PlainText
    workflow: Workflow
    style: Style = None
    accessibility_label: str = None

    @validator("text")
    def text_validator(cls, value: PlainText) -> PlainText:
        if len(value.text) > 75:
            raise ValueError("text should be less than 75 char")
        return value

    @validator("accessibility_label")
    def accessibility_label_validator(cls, value: str) -> str:
        if len(value) > 75:
            raise ValueError("accessibility label should be less than 75 char")
        return value
