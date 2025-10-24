from Modules.Items.Items import Item
from Resources.Data.Enums import Values
import logging as lg


class UniversalInventory:
    def __init__(self, max_weight_gramm, max_weapon, max_armor):
        self.inv = []
        self.max_weight_gramm: int = max_weight_gramm
        self.max_weapon: int = max_weapon
        self.max_armor: int = max_armor
        self.weight_count: int = 0
        self.weapon_count: int = 0
        self.armor_count: int = 0

    def __add__(self, other):
        if not type(other) == type(Item):
            if not other.__bases__[0] == type(Item):
                lg.warn(f"{other} has an interesting type...")

        if self.weight_count + other.weight_gramm > self.max_weight_gramm:
            lg.debug("Can not add item, to heavy")
            return
        if other.group == Values.WEAPON:
            if self.weapon_count == self.max_weapon:
                lg.debug("Can no add another weapon")
                return
        if other.group == Values.WEAPON:
            if self.armor_count == self.max_armor:
                lg.debug("Can no add another armor")
                return

        self.inv.add(other)

    def __sub__(self, other):
        searched: str = other.name

        for item in self.inv:
            if item.name == searched:
                self.inv.remove(item)
                return
        else:
            lg.debug(f"Item {searched} not in inventory")
            return

    def get_content(self) -> dict[str:int]:
        pr_dict: dict[str:int] = {}

        for item in self.inv:
            if item.name not in pr_dict:
                pr_dict.update({item.name : 1})
            else:
                pr_dict[item.name] += 1

        return pr_dict

    def __str__(self):
        content: dict[str:int] = self.get_content()
        pr_str: str = ""

        for name, amount in content:
            pr_str += f"{name}\t{amount}\n"

        return pr_str

    def switch(self, item_to_remove, item_to_add):
        raise NotImplementedError("Not yet Bro")

