import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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
    
    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "text")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_props(self):
        child = LeafNode("span", "hello")
        parent = ParentNode("a", [child], {"href": "https://google.com<"})
        self.assertEqual(
            parent.to_html(),
            '<a href="https://google.com<"><span>hello</span></a>'
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "ul",
            [
                LeafNode("li", "item 1"),
                LeafNode("li", "item 2"),
                LeafNode("li", "item 3"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<ul><li>item 1</li><li>item 2</li><li>item 3</li></ul>"
        )

    def test_to_html_nested_parents(self):
        inner = ParentNode("p", [LeafNode("b", "bold")])
        outer = ParentNode("div", [inner])
        self.assertEqual(
            outer.to_html(),
            "<div><p><b>bold</b></p></div>"
        )

    def test_to_html_deeply_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode("p", [LeafNode(None, "deep text")])
                    ]
                )
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><section><p>deep text</p></section></div>"
        )


if __name__ == "__main__":
    unittest.main()