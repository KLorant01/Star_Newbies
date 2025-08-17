class que:
    def __init__(self) ->  None:
        self.queList: list[str] = []

    def contains(self, msg: str) -> bool:
        return msg in self.queList
