from .block_elements import UrlInputExamples
from slackuiblocks import Blocks
from slack_sdk import WebClient

TOKEN = "xoxb-5685149968484-5718507706929-d1Dx7sldxzzxGVsBlPAKT7QY"


def create_blocks():
    blocks = Blocks()
    blocks.blocks.append(UrlInputExamples())
    breakpoint()
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
