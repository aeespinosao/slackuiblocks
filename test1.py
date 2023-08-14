from slack_sdk import WebClient
from layout_blocks import Section
from composition_objects import Text, TextType
TOKEN="xoxb-5685149968484-5718507706929-9BrcHKfII9zIli1zkMDKIbjB"
import json

from pydantic import BaseModel

class Blocks(BaseModel):
    blocks: list[Section] = []

def create_blocks() -> Blocks:
    blocks =  Blocks()
    blocks.blocks.append(
        Section(
            text=Text(
                type=TextType.MARKDOWN, 
                text="You have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*"
            )
        )
    )
    #blocks.blocks.append(Section(
    #    fields=[
    #        Text(TextType.MARKDOWN, "*Type:*\nComputer (laptop)"),
    #        Text(TextType.MARKDOWN, "*When:*\nSubmitted Aut 10"),
    #        Text(TextType.MARKDOWN, "*Last Update:*\nMar 10, 2015 (3 years, 5 months)"),
    #        Text(TextType.MARKDOWN, "Reason:*\nAll vowel keys aren't working."),
    #        Text(TextType.MARKDOWN, "*Specs:*\n\"Cheetah Pro 15\" - Fast, really fast\""),
    #    ]
    #))
    result = blocks.dict(exclude_none=True).get("blocks")
    for r in result:
        del r['text']['emoji']
    print(json.dumps(result))
    return result

client = WebClient(token=TOKEN)
try:
    response = client.chat_postMessage(
        channel="C05LF9Z323B",
        text='message',
        blocks=json.dumps(create_blocks()),
        
    )
except Exception as e:
    # You will get a SlackApiError if "ok" is False
    print( e.response["error"] )
    


    
    
"""[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "You have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*"
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": "*Type:*\nComputer (laptop)"
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*When:*\nSubmitted Aut 10"
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Last Update:*\nMar 10, 2015 (3 years, 5 months)"
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Reason:*\nAll vowel keys aren't working."
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Specs:*\n\"Cheetah Pro 15\" - Fast, really fast\""
                        }
                    ]
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "emoji": True,
                                "text": "Approve"
                            },
                            "confirm": {
                                "title": {
                                    "type": "plain_text",
                                    "text": "Are you sure?"
                                },
                                "text": {
                                    "type": "mrkdwn",
                                    "text": "Wouldn't you prefer a good game of _chess_?"
                                },
                                "confirm": {
                                    "type": "plain_text",
                                    "text": "Do it"
                                },
                                "deny": {
                                    "type": "plain_text",
                                    "text": "Stop, I've changed my mind!"
                                }
                            },
                            "style": "primary",
                            "value": "click_me_123"
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "emoji": True,
                                "text": "Deny"
                            },
                            "style": "danger",
                            "value": "click_me_123"
                        }
                    ]
                }
            ]"""