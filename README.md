# slackuiblocks - Simplify Slack UI Block Creation with Python Classes

[![PyPI Version](https://img.shields.io/pypi/v/slackuiblocks)](https://pypi.org/project/slackuiblocks/)
[![License](https://img.shields.io/github/license/aeepsinosao/slackuiblocks)](https://github.com/aeespinosao/slackuiblocks/blob/main/LICENSE)

`slackuiblocks` is a Python library that provides an intuitive and elegant way to create Slack UI blocks using Python classes instead of dealing with complex JSON structures. With this library, you can easily craft interactive and visually appealing messages for your Slack channels or direct messages.

## Features

- **Simplified Syntax**: Define Slack UI blocks using Python classes, making it easier to structure your messages.
- **Interactive Elements**: Create buttons, menus, and other interactive components effortlessly.
- **Customization**: Customize the appearance and behavior of UI elements using Python attributes.
- **Well-Organized**: Maintain a clear and organized codebase by encapsulating UI elements within classes.

## Installation

You can install `slackuiblocks` using pip:

```bash
pip install slackuiblocks
```

## Usage Example

Here's a simple example of how you can use `slackuiblocks` to create a message with interactive buttons:

```python
from slack_sdk import WebClient
from slackuiblocks import Section, MarkdownText, Datepicker, PlainText

message = Blocks(
    blocks=[
        Section(
            text=MarkdownText(
                text=(
                    "*Sally* has requested you set the deadline for the Nano "
                    "launch project"
                )
            ),
            accessory=Datepicker(
                action_id="datepicker123",
                initial_date="1990-04-28",
                placeholder=PlainText(text="Select a date"),
            ),
        )
    ]
)

# Get the JSON representation of the block
block_json = message.dict(exclude_none=True)

# Use block_json in your Slack API request
channel = "your channel id"
try:
    client.chat_postMessage(
        channel=channel,
        text="message",
        blocks=block_json.get("blocks"),
    )
except Exception as e:
    print(e)
```

For more complex interactions, you can create menus, input fields, and more using Python classes just like the example above.

## Documentation

For detailed usage instructions, examples, and a comprehensive list of available UI elements, refer to the [Documentation](https://github.com/aeespinosao/slackuiblocks/blob/main/docs/README.md).

## Contributing

Contributions are welcome! To contribute to `slackuiblocks`, follow the guidelines outlined in [CONTRIBUTING.md](https://github.com/aeespinosao/slackuiblocks/blob/main/CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](https://github.com/aeespinosao/slackuiblocks/blob/main/LICENSE).
