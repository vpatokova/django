class DogOrFogConverter:
    regex = "([df]og)"

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)


class PositiveNumberConverter:
    regex = "([1-9]\d*)"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
