from .block_elements import UrlInputExamples
from pydantic import BaseModel
from slackuiblocks.layout_blocks import Section
from slack_sdk import WebClient

TOKEN = "xoxb-5685149968484-5718507706929-9BrcHKfII9zIli1zkMDKIbjB"


class Blocks(BaseModel):
    blocks: list[Section] = []


def create_blocks():
    blocks = Blocks()
    blocks.blocks.append(UrlInputExamples())
    return blocks.dict(exclude_none=True).get("blocks")


def main():
    client = WebClient(token=TOKEN)
    # print(json.dumps(create_blocks()))
    try:
        client.chat_postMessage(
            channel="C05LF9Z323B",
            text="message",
            blocks=create_blocks(),
        )
    except Exception as e:
        # You will get a SlackApiError if "ok" is False
        print(e)


main()
