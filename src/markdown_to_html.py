from blocks_markdown import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import ParentNode, LeafNode
from markdowninterpreter import text_to_textnodes
from textnode import text_node_to_html_node

block_type_dict = { 
        BlockType.PARAGRAPH : ("p", None),
        BlockType.HEADING : ("h2", None),
        BlockType.CODE : ("pre", "code"),
        BlockType.QUOTE : ("blockquote", "p"),
        BlockType.ULIST : ("ul", "li"),
        BlockType.OLIST : ("ol", "li"),
    }

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type, has_children = block_to_block_type(block)
        if has_children:
            children = md_block_to_children_nodes(block, block_type)
            html_nodes.append(ParentNode(block_type_dict[block_type][0], children, None))
        elif block_type == BlockType.CODE:
            child = LeafNode("code", block[3:-3], None)
            html_nodes.append(ParentNode("pre", [child], None))
        else:
            children = inline_text_to_text_nodes(block)
            html_nodes.append(ParentNode(block_type_dict[block_type][0], children, None))


    return ParentNode("div", html_nodes, None)

def md_block_to_children_nodes(markdown_block, block_type):
    items = markdown_block.split("\n")
    child_nodes = []
    for item in items:
        grandchild_nodes = inline_text_to_text_nodes(item)
        child_node = ParentNode(block_type_dict[block_type][1], grandchild_nodes, None)
        child_nodes.append(child_node)
    
    return child_nodes


def inline_text_to_text_nodes(text):
    text = text.replace("\n", " ")
    child_text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in child_text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    return html_nodes