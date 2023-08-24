from .block_elements import UrlInputExamples
from slackuiblocks import Blocks
from slack_sdk import WebClient

TOKEN = ""


def create_blocks():
    blocks = Blocks()
    blocks.blocks.append(UrlInputExamples())
    return blocks.to_dict()


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
