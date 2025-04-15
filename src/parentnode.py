from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    #tag - A string representing the HTML tag name e.g "p", "a", "h1" etc...
    # value - A string representing the value of the HTML tag
    # props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag cannot be null")
        elif not self.children or len(self.children) == 0:
            raise ValueError("parent must have a child")
        
        html_str = ""
        for child in self.children:
            html_str += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{html_str}</{self.tag}>"     