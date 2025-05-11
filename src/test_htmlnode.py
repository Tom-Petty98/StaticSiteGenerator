import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode


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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_2(self):
        bold_txt = LeafNode("b", "Bold text")
        normal_txt = LeafNode(None, "Normal text")
        italic_txt = LeafNode("i", "italic text")
        parent = ParentNode("p", [bold_txt, normal_txt, italic_txt, normal_txt])
        link = LeafNode("a", "Click me!", {"href" : "https://www.google.com"})
        parent2 = ParentNode("p", [link])
        grandparent = ParentNode("div", [parent, parent2])
        self.assertEqual(
            grandparent.to_html(),
            "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><a href=\"https://www.google.com\">Click me!</a></p></div>"
        )

    # def test_to_html_no_tag(self):
    #     child_node = LeafNode("span", "child")
    #     parent_node = ParentNode(None, [child_node])
    #     self.assertRaises(ValueError, node.to_html())

        # def test_to_html_no_children(self):
    #     parent_node = ParentNode("div", [])
    #     self.assertRaises(ValueError, node.to_html())

    # def test_to_html_no_children2(self):
    #     parent_node = ParentNode("div", None)
    #     self.assertRaises(ValueError, node.to_html())

class TestLeafNode(unittest.TestCase):
    # def test_to_html_no_value(self):
    #     node = LeafNode("p", None, None)
    #     self.assertRaises(ValueError, node.to_html())

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Raw text", None)
        html = node.to_html()
        self.assertEqual(html, "Raw text")

    def test_props_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        html = node.to_html()
        self.assertEqual(html, "<a href=\"https://www.google.com\">Click me!</a>")

    def test_props_to_html_img(self):
        node = LeafNode("img", "", {"src" : "https://www.image.com", "alt": "alt text"})
        html = node.to_html()
        self.assertEqual(html, "<img src=\"https://www.image.com\" alt=\"alt text\"></img>")

if __name__ == "__main__":
    unittest.main()