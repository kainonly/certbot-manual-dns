class Qcloud:
    def __init__(self, id, key):
        self.id = id
        self.key = key

    def resolve(self, subDomain, record) -> bool:
        return True
