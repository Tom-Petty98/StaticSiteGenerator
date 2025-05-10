import unittest
from textnode import TextNode, TextType
from markdowninterpreter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TestMarkdowninterpreter(unittest.TestCase):
    # def test_to_html_odd_delimiter_count(self):
    #     node = TextNode("Text node`", TextType.TEXT)       
    #     self.assertRaises(Exception, split_nodes_delimiter([node], "`", TextType.CODE))

    def test_split_no_change(self):
        node = TextNode("Text node", TextType.TEXT)
        node2 = TextNode("Text node2", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextType.BOLD)
        self.assertEqual([node, node2], new_nodes)

    # def test_text_bold_multi_split(self):
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


    def test_extract_markdown_no_images(self):
        matches = extract_markdown_images(
            "This is text with no images heres a link instead [GitHub link](https://github.com)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_multiple_images(self):
        matches = extract_markdown_images(
            "Here is an image ![Example Image](https://example.com/image.jpg) and another ![Second](https://example.com/second.jpg)"
        )
        self.assertListEqual([('Example Image', 'https://example.com/image.jpg'), ('Second', 'https://example.com/second.jpg')], matches)

    def test_extract_markdown_no_links(self):
        matches = extract_markdown_links(
            "This is text with no links here is an image instead ![Example Image](https://example.com/image.jpg) and another ![Second](https://example.com/second.jpg)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_multiple_links(self):
        matches = extract_markdown_links(
            "Here is a [GitHub link](https://github.com) and another [Python site](https://www.python.org)"
        )
        self.assertListEqual([('GitHub link', 'https://github.com'), ('Python site', 'https://www.python.org')], matches)

if __name__ == "__main__":
    unittest.main()