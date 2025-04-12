import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_textType_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_url_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "url")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Bold", TextType.BOLD, "url")
        node_str = node.__repr__()
        self.assertNotEqual(node_str, "TextNode(Bold, This is a bold text node, url)")



if __name__ == "__main__":
    unittest.main()