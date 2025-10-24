from Resources.Data.Enums import Values


class Item:
    def __init__(self, name, cost, weight_gramm):
        self.group = Values.ITEM
        self.name: str = name
        self.cost: int = cost
        self.weight_gramm: int = weight_gramm


class Weapons(Item):
    def __init__(self, name, cost, weigh_gramm):
        super.__init__(name, cost, weigh_gramm)
        self.group = Values.WEAPON

    def attack(self):
        pass


class Armor(Item):
    def __init__(self, name, cost, weigh_gramm, protection_bonus: int, dmg_reduction: float):
        super.__init__(name, cost, weigh_gramm)
        self.group = Values.ARMOR
        self.protection_bonus = protection_bonus
        if dmg_reduction > 1 or dmg_reduction < 0:
            raise Exception("Armor to op")
        self.dmg_reduction = dmg_reduction

    def protect(self, dmg: int):
        return round(self.dmg_reduction * dmg)


class Gadget(Item):
    def __init__(self, name, cost, weigh_gramm):
        super.__init__(name, cost, weigh_gramm)
        self.group = Values.GADGET


class Trinket(Item):
    def __init__(self, name, cost, weigh_gramm, rarity: str = "common"):
        super.__init__(name, cost, weigh_gramm)
        self.group = Values.TRINKET
        self.rarity: str = rarity


class Food(Item):
    def __init__(self, name, cost, weigh_gramm):
        super.__init__(name, cost, weigh_gramm)
        self.group = Values.FOOD


class Part(Item):
    def __init__(self, name, cost, weigh_gramm):
        super.__init__(name, cost, weigh_gramm)
        self.group = Values.PART

