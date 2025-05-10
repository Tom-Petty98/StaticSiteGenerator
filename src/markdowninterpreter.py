from textnode import TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        delimiter_count = node.text.count(delimiter)
        if delimiter_count % 2 != 0:
            raise Exception(f"missing a closing {delimiter}")
        
        if delimiter_count > 0:
            split_text = node.text.split(delimiter)
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], node.text_type))
            new_nodes.append(TextNode(split_text[1], text_type))
            if split_text[2] != "":
                new_nodes.append(TextNode(split_text[2], node.text_type))
        else:
            new_nodes.append(node)

    return new_nodes



def extract_markdown_images(text):
    ## Markdown image pattern: ![alt text](image_url)
    return re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", text)

def extract_markdown_links(text):
    ## Markdown link pattern: [link text](url)
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
