import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("img", None, None, {"src" : "https://www.image.com", "alt": "alt text"})
        node_str = node.__repr__()
        self.assertEqual(node_str, "HTMLNode(img, None, None, {'src': 'https://www.image.com', 'alt': 'alt text'})")

    def test_repr_2(self):
        node1 = HTMLNode("img", {"src" : "https://www.image.com", "alt": "alt text"})
        node = HTMLNode("div", None, [node1], None)
        node_str = node.__repr__()
        self.assertEqual(node_str, "HTMLNode(div, None, [HTMLNode(img, {'src': 'https://www.image.com', 'alt': 'alt text'}, None, None)], None)")

    def test_props_to_html_None(self):
        node = HTMLNode("div", None, None, None)
        props_str = node.props_to_html()
        self.assertEqual(props_str, "")

    def test_props_to_html_Empty(self):
        node = HTMLNode("div", None, None, {})
        props_str = node.props_to_html()
        self.assertEqual(props_str, "")

    def test_props_to_html_2(self):
        node = HTMLNode("img", None, None, {"src" : "https://www.image.com", "alt": "alt text"})
        props_str = node.props_to_html()
        self.assertEqual(props_str, " src=\"https://www.image.com\" alt=\"alt text\"")


if __name__ == "__main__":
    unittest.main()