class stdio():
    def __init__(self, language: str) -> None:
        self.language = language
        pass

    def scanf(self, content: dict):
        return input(content[self.language])

    def printf(self, content: dict):
        return print(content[self.language])