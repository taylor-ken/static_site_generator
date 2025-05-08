import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_empty_props(self):
        # Test that an HTMLNode with no props returns an empty string
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_one_prop(self):
        # Test a node with a single property
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
        
    def test_props_to_html_with_multiple_props(self):
        # Test a node with multiple properties
        node = HTMLNode(props={
            "href": "https://example.com",
            "target": "_blank",
            "class": "link"
        })
        # Note: order of props might vary, so this might need adjustment
        self.assertTrue(' href="https://example.com"' in node.props_to_html())
        self.assertTrue(' target="_blank"' in node.props_to_html())
        self.assertTrue(' class="link"' in node.props_to_html())

    def test_repr(self):
        # Create a node with some attributes
        node = HTMLNode(tag="a", value="Click me", children=None, props={"href": "https://example.com"})
        
        # Get the string representation
        repr_str = repr(node)
        
        # Check that the representation includes all the important parts
        # You don't need to check the exact format, just that all info is present
        self.assertIn("tag=a", repr_str)
        self.assertIn("value=Click me", repr_str)
        self.assertIn("children=None", repr_str)
        self.assertIn("href", repr_str)
        self.assertIn("https://example.com", repr_str)

if __name__ == "__main__":
    unittest.main()