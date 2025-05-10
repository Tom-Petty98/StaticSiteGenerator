from textnode import TextNode, TextType
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


def split_nodes_with_links(old_nodes):
    ## Markdown link pattern: [link text](url)
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return create_text_nodes(old_nodes, pattern, TextType.LINK)

def split_nodes_with_images(old_nodes):
    ## Markdown image pattern: [link text](url)
    pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    return create_text_nodes(old_nodes, pattern, TextType.IMAGE)


def create_text_nodes(old_nodes, pattern, text_type):
    extracted_items = []
    for node in old_nodes:
        extracted_items.extend(extract_markdown_link_or_image_nodes(node.text, pattern))

    new_nodes = []
    for item in extracted_items:
        if type(item) is tuple:
            new_nodes.append(TextNode(item[0], text_type, item[1]))
        else:
            new_nodes.append(TextNode(item, TextType.TEXT))

    return new_nodes

def extract_markdown_link_or_image_nodes(text, pattern):    
    matches = list(re.finditer(pattern, text))  # Find all matches with positions
    result = []
    last_index = 0

    for match in matches:
        start, end = match.span()
        result.append(text[last_index:start]) # Add preceding text
        result.append((match.group(1), match.group(2)))  # Add link as tuple
        last_index = end

    result.append(text[last_index:].strip())  # Add remaining text after last match
    return [item for item in result if item]  # Remove empty entries