from .block_elements import *
from pydantic import BaseModel
from slackuiblocks.layout_blocks import Section
from slack_sdk import WebClient
import json

TOKEN=""


class Blocks(BaseModel):
    blocks: list[Section] = []

def create_blocks():
    blocks =  Blocks()
    blocks.blocks.append(
        UrlInputExamples()
    )
    return blocks.dict(exclude_none=True).get("blocks")
    
def main():
    client = WebClient(token=TOKEN)
    # print(json.dumps(create_blocks()))
    try:
        response = client.chat_postMessage(
            channel="C05LF9Z323B",
            text='message',
            blocks=json.dumps(create_blocks()),   
        )
    except Exception as e:
        # You will get a SlackApiError if "ok" is False
        print(e) 

#main()