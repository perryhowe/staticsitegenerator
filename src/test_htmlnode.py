import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="p", value="hello", props={
        "href": "https://www.google.com",
        "target": "_blank",
    })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_empty_dict(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_repr(self):
        node = HTMLNode("p", "hello", None, {"class": "text"})
        self.assertEqual("HTMLNode(p, hello, None, {'class': 'text'})", repr(node))


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "google.com", {"href": "https://google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://google.com">google.com</a>',
        )

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "raw text")
        self.assertEqual(node.to_html(), "raw text")

    def test_leaf_repr(self):
        node = LeafNode("p", "hello", {"class": "text"})
        self.assertEqual(
            node.__repr__(),
            "LeafNode(p, hello, {'class': 'text'})",
    )


if __name__ == "__main__":
    unittest.main()