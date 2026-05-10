"""Email validation utility (POC scaffold from Jira requirements)."""
from __future__ import annotations

import re

# Practical syntax-focused check (not a full RFC 5322 parser).
_EMAIL_RE = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$"
)


def is_valid_email(value: str) -> bool:
    if not isinstance(value, str):
        return False
    s = value.strip()
    if not s or " " in s or len(s) > 254:
        return False
    return bool(_EMAIL_RE.match(s))
