class HTMLNode():
    #tag - A string representing the HTML tag name e.g "p", "a", "h1" etc...
    # value - A string representing the value of the HTML tag (can have no value but in this case should have children)
    # children - A list of HTMLNode objects
    # props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    def __init__(self, tag = None, value = None, chidren = None, props = None):
        self.tag = tag
        self.value = value
        self.children = chidren
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