
class HTMLNode():
    #tag - A string representing the HTML tag name e.g "p", "a", "h1" etc...
    # value - A string representing the value of the HTML tag (can have no value but in this case should have children)
    # children - A list of HTMLNode objects
    # props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        html_atr = ""
        for atr in self.props:
            html_atr += f" {atr}=\"{self.props[atr]}\""
        return html_atr
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class ParentNode(HTMLNode):
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


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("value cannot be null")
        elif not self.tag:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"