from lib.util.string import normalize


class Tika:
    def __init__(self, parser):
        self.__parser = parser
        super().__init__()

    def set_link(self, link):
        self.__link = link

    def get_text(self):
        raw = self.__parser.from_file(self.__link)
        return normalize(raw['content'])
