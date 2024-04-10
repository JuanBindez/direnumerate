

class DirenumerateException(Exception):
    "base exception for Direnumerate."


class DirenumerateError(DirenumerateException):
    def __init__(self, mensage):
        super().__init__(mensage)
        self.mensage = mensage
