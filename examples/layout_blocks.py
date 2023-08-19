from slackuiblocks import (
    Actions,
    SelectStatic,
    PlainText,
    Option,
    Button,
    Context,
    Image,
    MarkdownText,
    Divider,
    Header,
    Input,
    PlainTextInput,
    Section,
    Datepicker,
    Video,
)


def ActionsExamples():
    return Actions(
        elements=[
            SelectStatic(
                placeholder=PlainText(text="Which witch is the witchiest witch?"),
                options=[
                    Option(text=PlainText(text="Matilda"), value="matilda"),
                    Option(text=PlainText(text="Glinda"), value="glinda"),
                ],
            ),
            Button(action_id="button_1", value="cancel", text=PlainText(text="Cancel")),
        ]
    )


def ContextExamples():
    return Context(
        elements=[
            Image(
                image_url="https://image.freepik.com/free-photo/red-drawing-pin_1156-445.jpg",
                alt_text="images",
            ),
            MarkdownText(text="Location: *Dogpatch*"),
        ]
    )


def DividerExamples():
    return Divider()


def HeaderExamples():
    return Header(text=PlainText(text="Budget Performance"))


def ImageExamples():
    return Image(
        title=PlainText(text="Please enjoy this photo of a kitten"),
        image_url="http://placekitten.com/500/500",
        alt_text="An incredibly cute kitten.",
    )


def InputExamples():
    return Input(
        element=PlainTextInput(),
        label=PlainText(text="Label :slightly_smiling_face:", emoji=True),
    )


def SectionExamples():
    def SimpleSection():
        return Section(
            text=MarkdownText(
                text="A message *with some bold text* and _some italicized text_."
            )
        )

    def TextFieldsSection():
        return Section(
            text=MarkdownText(
                text="A message *with some bold text* and _some italicized text_."
            ),
            fields=[
                MarkdownText(text="High"),
                PlainText(text="String"),
                PlainText(text="Low"),
            ],
        )

    def AccesorySection():
        return Section(
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

    return [SimpleSection(), TextFieldsSection(), AccesorySection()]


def VideoExamples():
    return Video(
        title=PlainText(text="How to use Slack."),
        title_url="https://www.youtube.com/watch?v=RRxQQxiM7AA",
        description=PlainText(
            text="Slack is a new way to communicate with your team. It"
        ),
        video_url="https://www.youtube.com/embed/RRxQQxiM7AA?feature=oembed&autoplay=1",
        alt_text="How to use Slack?",
        thumbnail_url="https://i.ytimg.com/vi/RRxQQxiM7AA/hqdefault.jpg",
        author_name="Arcado Buendia",
        provider_name="YouTube",
        provider_icon_url="https://a.slack-edge.com/80588/img/unfurl_icons/youtube.png",
    )
