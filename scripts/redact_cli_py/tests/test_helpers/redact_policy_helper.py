

import re


class RedactPolicyHelper:
    @staticmethod
    def is_first_char(text: str) -> bool:
        # There is no alphanumeric char except Aa0.
        return re.match("^[b-zB-Z1-9]*$", text) is None
