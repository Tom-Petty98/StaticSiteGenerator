from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "<p></p>"
    HEADING = "<h2></h2>"
    CODE = "code block"
    QUOTE = "quote block"
    ULIST = "<ul></ul>"
    OLIST = "<ol></ol>"

#Returns block type and wheather the block has children
def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING, False
    elif block[0:3] == "```":
        return BlockType.CODE, False
    
    quote_block = True
    ul_block = True
    ol_block = True
    lines = block.split("\n")
    count = 1
    for line in lines:
        if line[0] != ">":
            quote_block = False
        if line[0:2] != "- ":
            ul_block = False
        if line[0:2] != f"{count}.":
            ol_block = False
        count += 1

    if quote_block == True:
        return BlockType.QUOTE, True
    elif ul_block == True:
        return BlockType.ULIST, True
    elif ol_block == True:
        return BlockType.OLIST, True
    return BlockType.PARAGRAPH, False


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return [b.strip() for b in blocks if b] # remove empty

