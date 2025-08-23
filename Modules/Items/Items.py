class Item:
    def __init__(self, name, cost, weight_gramm):
        self.name: str = name
        self.cost: int = cost
        self.weight_gramm: int = weight_gramm


class Weapones(Item):
    def __init__(self, name, cost, weigh_gramm):
        super.__init__(name, cost, weigh_gramm)


class Armore(Item):
    def __init__(self, name, cost, weigh_gramm):
        super.__init__(name, cost, weigh_gramm)
