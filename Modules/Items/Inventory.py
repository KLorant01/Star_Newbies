from Items import Item

class Invetory():
    def __init__(self):
        self.storage: dict[Item:int] = {}
        self.weight: int = 0

    def add(self, item: Item, quantity: int) -> None:
        if item in self.storage:
            self.storage[item] += quantity
        else:
            self.storage.update({item : quantity})
        return

    def rem(self, item: Item, quantity: int) -> True | False:
        if item not in self.storage:
            return False
        else:
            if self.storage[item] - quantity > 0:
                self.storage[item] -= quantity
                return True

            elif self.storage[item] - quantity == 0:
                self.storage.pop(item)
                return True

            else:
                return False