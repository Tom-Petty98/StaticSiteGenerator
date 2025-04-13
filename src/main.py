from textnode import TextNode, TextType
from leafnode import LeafNode

def main():
    obj = TextNode("Hello world", TextType.LINK, "https://www.static.site")
    leaf_node = LeafNode("p", None, None)
    leaf_node.to_html()
    print(obj)

main()