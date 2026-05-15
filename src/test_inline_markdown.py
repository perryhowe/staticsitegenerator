import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_delim_bold_double(self):
        node = TextNode("This is text with **two** words that are **bold**, ok?", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("two", TextType.BOLD),
                TextNode(" words that are ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(", ok?", TextType.TEXT)
            ],
            new_nodes
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_italic(self):
        node = TextNode("This is text with an _italic_ word AND a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word AND a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_delim_unmatched(self):
        node = TextNode("This has an **unmatched bold", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images("This text has no images at all")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_ignores_images(self):
        matches = extract_markdown_links(
            "![an image](https://example.com/img.png) and [a link](https://example.com)"
        )
        self.assertListEqual([("a link", "https://example.com")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "![cat](https://example.com/cat.png) and ![dog](https://example.com/dog.png)"
        )
        self.assertListEqual(
            [
                ("cat", "https://example.com/cat.png"),
                ("dog", "https://example.com/dog.png"),
            ],
            matches,
        )

    def test_extract_markdown_images_empty_alt(self):
        matches = extract_markdown_images("![](https://example.com/img.png)")
        self.assertListEqual([("", "https://example.com/img.png")], matches)

if __name__ == "__main__":
    unittest.main()