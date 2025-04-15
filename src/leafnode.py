from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    #tag - A string representing the HTML tag name e.g "p", "a", "h1" etc...
    # value - A string representing the value of the HTML tag
    # props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("value cannot be null")
        elif not self.tag:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    