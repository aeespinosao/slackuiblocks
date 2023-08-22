from layout_blocks import Section
from pydantic import BaseModel


class Blocks(BaseModel):
    blocks: list[Section] = []
