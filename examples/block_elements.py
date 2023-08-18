
from slackuiblocks import *

def ButtonExamples():
    # Regular interactive button
    button = Button(
        text=PlainText(text="Click Me"),
        value="click_me_123",
        action_id="button", 
    )
        
    # A button with a primary style attribute
    primary_button = Button(
        text=PlainText(text="Save"),
        style=Style.PRIMARY,
        value="click_me_123",
        action_id="button2", 
    )
    
    # Link button
    link_button = Button(
        text=PlainText(text="Link Button"),
        url="https://api.slack.com/block-kit"  
    )
    
    return Actions(elements=[button, primary_button, link_button])

def CheckboxExamples():
    checkbox = CheckboxGroups(
        action_id="this_is_an_action_id",
        initial_options=[
            Option(
                value="A1",
                text=PlainText(text="Checkbox 1")
            )
        ],
        options=[
            Option(
                value="A1",
                text=PlainText(text="Checkbox 1")
            ), 
            Option(
                value="A2",
                text=PlainText(text="Checkbox 2")
            )
            
        ]
    )
    
    return Section(text=PlainText(text="Check out these charming checkboxes"),accessory=checkbox)

def DatepickerExamples():
    datepicker = Datepicker(
        action_id="datepicker123",
        initial_date="1990-04-28",
        placeholder=PlainText(
            text="Select a date"
        )
    )
    return Section(text=PlainText(text="Pick a date for the deadline."),accessory=datepicker)

def DatetimepickerExamples():
    datetimepicker = Datetimepicker(
        action_id="datetime_input",
        initial_date_time=1628633820
    )
    return Actions(elements=[datetimepicker])
    
def EmailInputExamples():
    email = EmailInput(
        action_id="email_text_input-action",
        placeholder=PlainText(
            text="Enter an email"
        )
    )
    return Input(label=PlainText(text="Email Address"),element=email)

def ImageExamples():
    image = Image(
        image_url="http://placekitten.com/700/500",
        alt_text="Multiple cute kittens"
    )
    
    return Context(elements=[image])


def MultiSelectExamples():
    def StaticOptions():
        return Section(
            text=PlainText(text="Pick items from the list"),
            accessory=MultiselectStatic(
                action_id="text1234",
                placeholder=PlainText(text="Select items"),
                options=[
                    Option(
                        text=PlainText(text="*this is plain_text text*"),
                        value="1"
                    ),
                    Option(
                        text=PlainText(text="*this is a markdown text*"),
                        value="2"
                    )
                ]
            )
        )
        
    def UserList():
        return Section(
            text=PlainText(text="Pick users from the list"),
            accessory=MultiselectUserList(
                action_id="text12",
                placeholder=PlainText(
                    text="_Select users_"
                )
            )
        )
    
    def ConversationList():
        return Section(
            text=PlainText(text="Pick conversations from the list"),
            accessory=MultiselectConversationList(
                action_id="text1",
                placeholder=PlainText(
                    text="Select conversations"
                )
            )
        )
        
    def PublicChannels():
        return Section(
            text=PlainText(text="Pick conversations from the list"),
            accessory=MultiselectPublicChannels(
                action_id="text",
                placeholder=PlainText(
                    text="Select channels"
                )
            )
        )
    
    return [StaticOptions(), UserList(), ConversationList(), PublicChannels()]
 

# TODO: Number input example


def OverflowExamples():
    return Section(
        text=MarkdownText(text="This is a section block with an overflow menu."),
        accessory=OverflowMenu(
            action_id="overflow",
            options=[
                Option(
                    text=PlainText(text="*this is plain_text text*"),
                    value="3"
                )
            ]
        )
    )
    
def InputExamples():
    return Input(
        label=PlainText(text="Label of input"),
        element=PlainTextInput(
            action_id="plain_input",
            placeholder=PlainText(text="Enter some plain text")
        )
    )
    
def RadioButtonExamples():
    return Section(
        text=PlainText(text="Check out these rad radio buttons"),
        accessory=RadioButton(
            action_id="this_is_an_action_id",
            options=[
                Option(
                    text=PlainText(
                        text="Radio 1"
                    ),
                    value="A1"
                )
            ]
        )
    )
    
def SelectExamples():
    def StaticOption():
        return Section(
            text=PlainText(text="Pick items from the list"),
            accessory=SelectStatic(
                action_id="text1234",
                placeholder=PlainText(text="Select item"),
                options=[
                    Option(
                        text=PlainText(text="*this is plain_text text*"),
                        value="1"
                    ),
                    Option(
                        text=PlainText(text="*this is a markdown text*"),
                        value="2"
                    )
                ]
            )
        )
        
    def UserList():
        return Section(
            text=PlainText(text="Pick users from the list"),
            accessory=SelectUser(
                action_id="text12",
                placeholder=PlainText(
                    text="Select user"
                )
            )
        )
    
    def ConversationList():
        return Section(
            text=PlainText(text="Pick conversations from the list"),
            accessory=SelectConversation(
                action_id="text1",
                placeholder=PlainText(
                    text="Select conversation"
                )
            )
        )
        
    def PublicChannel():
        return Section(
            text=PlainText(text="Pick conversations from the list"),
            accessory=SelectPublicChannel(
                action_id="text",
                placeholder=PlainText(
                    text="Select channel"
                )
            )
        )
    
    return [StaticOption(), UserList(), ConversationList(), PublicChannel()]
 
def TimepickerExamples():
    timepicker = TimePicker(
        action_id="timepicker123",
        timezone="America/Los_Angeles",
        initial_date="12:20",
        placeholder=PlainText(
            text="Select time"
        )
    )
    return Section(text=PlainText(text="Pick a date for the deadline."),accessory=timepicker)

def UrlInputExamples():
    return Input(
        label=PlainText(text="Label of url input"),
        element=UrlInput(
            action_id="url_text_input-action",
        )
    )