import re


class PoopOrLoopConverter:
    regex = r"[pl]oop"

    def to_python(self, value: str):
        if re.search(self.regex, value):
            return value
        else:
            raise ValueError

    def to_url(self, value):
        return value
