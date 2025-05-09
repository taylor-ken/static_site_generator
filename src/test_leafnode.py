import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_tag_with_attributes(self):
        node = LeafNode("a", "Text", {'href': 'link', 'target': '_blank'})
        self.assertEqual(node.to_html(), '<a href="link" target="_blank">Text</a>')

    def test_no_tag(self):
        node = LeafNode("a", "text")
        self.assertEqual(node.to_html(), '<a>text</a>')

    def test_none_tag(self):
        node = LeafNode(None, "text")
        self.assertEqual(node.to_html(), 'text')
