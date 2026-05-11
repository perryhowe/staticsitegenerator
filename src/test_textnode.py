import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq_text(self):
        node = TextNode("My name is Perry", TextType.BOLD)
        node2 = TextNode("My name isn't Perry", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteq_texttype(self):
        node = TextNode("My name is Perry", TextType.ITALIC)
        node2 = TextNode("My name is Perry", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, url=None)
        node2 = TextNode("This is a text node", TextType.BOLD, url=None)
        self.assertEqual(node, node2)

    def test_noteq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, url=None)
        node2 = TextNode("This is a text node", TextType.BOLD, url="https://github.com/perryhowe")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()