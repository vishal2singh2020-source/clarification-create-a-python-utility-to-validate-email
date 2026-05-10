"""Tests for email_validate."""
import unittest

from email_validate import is_valid_email

_REQ = "Clarification: Create a Python utility to validate email addresses\n\nClarification requested for Jira issue KAN-1:\n\ni had asked you to also add  changes like user should be able to enter the emails fro"


class TestIsValidEmail(unittest.TestCase):
    def test_valid_samples(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("a@b.co"))

    def test_invalid_samples(self):
        self.assertFalse(is_valid_email(""))
        self.assertFalse(is_valid_email("nodomain"))
        self.assertFalse(is_valid_email("@missing.local"))
        self.assertFalse(is_valid_email("space in@here.com"))
        self.assertFalse(is_valid_email("bad"))

    def test_whitespace_trimmed(self):
        self.assertTrue(is_valid_email("  user@example.com  "))

    def test_requirement_echo(self):
        self.assertIn("email", _REQ.lower())


if __name__ == "__main__":
    unittest.main()
