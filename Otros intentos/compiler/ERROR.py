class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result


class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)


class ExpectedCharError(Error):
    def __init__(self, details):
        super().__init__('Expected Character', details)


class InvalidSyntaxError(Error):
    def __init__(self, details=''):
        super().__init__('Invalid Syntax', details)
