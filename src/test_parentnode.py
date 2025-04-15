import unittest
from parentnode import ParentNode
from leafnode import LeafNode

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


if __name__ == "__main__":
    unittest.main()