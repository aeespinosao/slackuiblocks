from pydantic import BaseModel, Field
from base_elements import Text, ConfirmationDialog, Option, DispatchActionConfig, OptionGroup, FilterConversarionList, Workflow
from enum import Enum

class ElementType(Enum):
    BUTTON="button"
    CHECKBOXES="checkboxes"
    DATEPICKER="datepicker"
    DATETIMEPICKER="datetimepicker"
    EMAILINPUT="email_text_input"
    IMAGE="image"
    MULTISELECTSTATIC="multi_static_select"
    MULTISELECTEXTERNALDATA="multi_external_select"
    MULTISELECTUSERLIST="multi_users_select"
    MULTISELECTCONVERSATIONLIST="multi_conversations_select"
    MULTISELECTCHANNELSLIST="multi_channels_select"
    NUMBERINPUT="number_input"
    OVERFLOWMENU="overflow"
    TEXTINPUT="text_input"
    RADIOBUTTON="radio_buttons"
    SELECTSTATIC="static_select"
    SELECTEXTERNALDATA="external_select"
    SELECTUSER="users_select"
    SELECTCONVERSATION="conversations_select"
    SELECTPUBLICCHANNEL="channels_select"
    TIMEPICKER="timepicker"
    URLINPUT="url_text_input"
    WORKFLOWBUTTON="workflow_button"
    
    
class Style(Enum):
    DEFAULT="default"
    PRIMARY="primary"
    DANGER="danger"
    
class Button(BaseModel):
    type: str = Field(ElementType.BUTTON, const=True)
    text: Text
    action_id: str
    url: str = None
    value: str = None
    style: Style = Style.DEFAULT
    confirm: ConfirmationDialog = None
    accessibility_label: str = None
    

class CheckboxGroups(BaseModel):
    type: str = Field(ElementType.CHECKBOXES, const=True)
    action_id: str
    options: list[Option]
    initial_options: list[Option] = []
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False
    

class Datepicker(BaseModel):
    type: str = Field(ElementType.DATEPICKER, const=True)
    action_id: str
    initial_date: str = None
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False
    placeholder: Text = None
    
    
class Datetimepicker(BaseModel):
    type: str = Field(ElementType.DATETIMEPICKER, const=True)
    action_id: str
    initial_date_time: int = None
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False
    
    
class EmailInput(BaseModel):
    type: str = Field(ElementType.EMAILINPUT, const=True)
    action_id: str
    initial_value: str = None
    dispatch_action_config: DispatchActionConfig = None
    focus_on_load: bool = False
    placeholder: Text = None
    

class Image(BaseModel):
    type: str = Field(ElementType.IMAGE, const=True)
    image_url: str
    alt_text: str
    

class Multiselect(BaseModel):
    action_id: str
    confirm: ConfirmationDialog = None
    max_selected_items: int = 1
    focus_on_load: bool = False
    placeholder: Text = None
    
    
class MultiselectStatic(Multiselect):
    type: str = Field(ElementType.MULTISELECTSTATIC, const=True)
    options: list[Option]
    option_groups: list[OptionGroup] = []
    initial_options: list[Option] = []
   
    
class MultiselectExternalData(Multiselect):
    type: str = Field(ElementType.MULTISELECTEXTERNALDATA, const=True) 
    min_query_length: int = 3
    initial_options: list[Option] = []


class MultiselectUserList(Multiselect):
    type: str = Field(ElementType.MULTISELECTEXTERNALDATA, const=True) 
    initial_users: list[str] = []
    
    
class MultiselectConversationList(Multiselect):
    type: str = Field(ElementType.MULTISELECTEXTERNALDATA, const=True) 
    initial_conversations: list[str] = []
    default_to_current_conversation: bool = False
    filter: FilterConversarionList = None


class MultiselectPublicChannels(BaseModel):
    type: str = Field(ElementType.MULTISELECTEXTERNALDATA, const=True) 
    initial_channels: list[str] = []


class NumberInput(BaseModel):
    type: str = Field(ElementType.NUMBERINPUT, const=True) 
    is_decimal_allowed: bool
    action_id: str = None
    initial_value: str = None
    min_value: str = None
    max_value: str = None
    dispatch_action_config: DispatchActionConfig = None
    focus_on_load: bool = False
    placeholder: Text = None


class OverflowMenu(BaseModel):
    type: str = Field(ElementType.OVERFLOWMENU, const=True) 
    action_id: str
    options: list[Option]
    confirm: ConfirmationDialog = None


class TextInput(BaseModel):
    type: str = Field(ElementType.TEXTINPUT, const=True) 
    action_id: str
    initial_value: str = None
    multiline: bool = False
    min_length: int = None
    max_length: int  = None
    dispatch_action_config: DispatchActionConfig = None
    focus_on_load: bool = False
    placeholder: Text = None
    
    
class RadioButton(BaseModel):
    type: str = Field(ElementType.RADIOBUTTON, const=True) 
    action_id: str
    options: list[Option]
    initial_option: list[Option] = []
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False
    

class SelectMenu(BaseModel):
    action_id: str
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False
    placeholder: Text = None
    

class SelectStatic(SelectMenu):
    type: str = Field(ElementType.SELECTSTATIC, const=True) 
    options: list[Option]
    option_groups: list[OptionGroup] = []
    initial_option: Option = None
    

class SelectExternalData(SelectMenu):
    type: str = Field(ElementType.SELECTEXTERNALDATA, const=True) 
    initial_option: Option = None
    min_query_length: int =  3


class SelectUser(SelectMenu):
    type: str = Field(ElementType.SELECTUSER, const=True) 
    initial_user: str
    

class SelectConversation(SelectMenu):
    type: str = Field(ElementType.SELECTCONVERSATION, const=True) 
    initial_conversation: str
    default_to_current_conversation: bool = False
    response_url_enabled: bool = False
    filter: FilterConversarionList = None


class SelectPublicChannel(SelectMenu):
    type: str = Field(ElementType.SELECTPUBLICCHANNEL, const=True) 
    initial_channel: str
    response_url_enabled: bool = False
    
    
class TimePicker(BaseModel):
    type: str = Field(ElementType.TIMEPICKER, const=True)
    action_id: str
    initial_time: str = None
    confirm: ConfirmationDialog = None
    focus_on_load: bool = False
    placeholder: Text = None
    timezone: str = None
    
    
class UrlInput(BaseModel):
    type: str = Field(ElementType.URLINPUT, const=True)
    action_id: str
    initial_value: str = None
    dispatch_action_config: DispatchActionConfig = None
    focus_on_load: bool = False
    placeholder: Text = None
    

class WorkflowButton(BaseModel):
    type: str = Field(ElementType.WORKFLOWBUTTON, const=True)
    text: Text
    workflow: Workflow
    style: Style = Style.DEFAULT
    accessibility_label: str = None