# -*- coding: utf-8 -*-


class Solution:

    def is_match(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in ('.', s[0])
        if len(p) >= 2 and p[1] == '*':
            if first_match:
                return self.is_match(s[1:], p) or self.is_match(s, p[2:])
            return self.is_match(s, p[2:])

        return first_match and self.is_match(s[1:], p[1:])
