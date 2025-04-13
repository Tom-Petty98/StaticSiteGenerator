import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    # def test_to_html_no_value(self):
    #     node = LeafNode("p", None, None)
    #     self.assertRaises(ValueError, node.to_html())

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Raw text", None)
        html = node.to_html()
        self.assertEqual(html, "Raw text")

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        html = node.to_html()
        self.assertEqual(html, "<p>This is a paragraph of text.</p>")

    def test_props_to_html_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        html = node.to_html()
        self.assertEqual(html, "<a href=\"https://www.google.com\">Click me!</a>")


if __name__ == "__main__":
    unittest.main()