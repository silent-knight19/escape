import unittest
from exporter import escape_html, generate_html_table


class TestHTMLExporter(unittest.TestCase):
    def test_normal_text_remains_unchanged(self):
        """Normal text without special characters should remain unchanged."""
        text = "Standard maintenance completed"
        self.assertEqual(escape_html(text), "Standard maintenance completed")

    def test_escapes_ampersand_and_less_than(self):
        """Text containing & and < should be escaped to &amp; and &lt;."""
        self.assertEqual(escape_html("Research & Development"), "Research &amp; Development")
        self.assertEqual(escape_html("if x < 10"), "if x &lt; 10")

    def test_escapes_greater_than_and_quotes(self):
        """Text containing > and quotes should be escaped to &gt; and &quot;."""
        self.assertEqual(escape_html("where latency > 250ms"), "where latency &gt; 250ms")
        self.assertEqual(escape_html('Status: "Pending"'), "Status: &quot;Pending&quot;")

    def test_table_generation_escapes_content(self):
        """Full table generation should contain escaped HTML entities."""
        records = [
            {"id": 1, "department": "R&D", "description": "x < 5", "status": '"OK"'}
        ]
        html = generate_html_table(records)
        self.assertIn("&amp;", html)
        self.assertIn("&lt;", html)
        self.assertIn("&quot;", html)
        self.assertNotIn("<td>R&D</td>", html)
        self.assertNotIn("<td>x < 5</td>", html)


if __name__ == "__main__":
    unittest.main()

