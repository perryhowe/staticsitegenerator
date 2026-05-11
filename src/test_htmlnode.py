import unittest

from htmlnode import HTMLNode


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