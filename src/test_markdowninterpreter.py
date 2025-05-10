import unittest
from textnode import TextNode, TextType
from markdowninterpreter import split_nodes_delimiter


class TestMarkdowninterpreter(unittest.TestCase):
    # def test_to_html_odd_delimiter_count(self):
    #     node = TextNode("Text node`", TextType.TEXT)       
    #     self.assertRaises(Exception, split_nodes_delimiter([node], "`", TextType.CODE))

    def test_split_no_change(self):
        node = TextNode("Text node", TextType.TEXT)
        node2 = TextNode("Text node2", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextType.BOLD)
        self.assertEqual([node, node2], new_nodes)

    # def test_text_bold_split(self):
    #     node = TextNode("Text **bold text** node **bold text 2**", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    #     expected = TextNode("Text ", TextType.TEXT)
    #     expected2 = TextNode("bold text", TextType.BOLD)
    #     expected3 = TextNode(" node **bold text 2**", TextType.TEXT)
    #     self.assertEqual(new_nodes, [expected, expected2, expected3])

    def test_text_italic_split(self):
        node = TextNode("_italic text_ normal text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected2 = TextNode("italic text", TextType.ITALIC)
        expected3 = TextNode(" normal text", TextType.TEXT)
        self.assertEqual(new_nodes, [expected2, expected3])

    def test_text_code_split(self):
        node = TextNode("Text `code text`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = TextNode("Text ", TextType.TEXT)
        expected2 = TextNode("code text", TextType.CODE)
        self.assertEqual(new_nodes, [expected, expected2])

if __name__ == "__main__":
    unittest.main()