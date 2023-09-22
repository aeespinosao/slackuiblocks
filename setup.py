import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="slackuiblocks",
    version="0.0.7",
    author="Andres Espinosa",
    description="Slack UI Blocks is a Python library that makes it easy to create and manage Slack UI blocks. It provides a high-level API that abstracts away the details of the Slack Block Kit JSON format, making it easy to build complex UIs with just a few lines of code.",  # noqa: E501
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["slackuiblocks"],
    install_requires=["pydantic>=1.10.4,<2.0.0"],
)
