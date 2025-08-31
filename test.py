import time
import dataclasses


def block(func):
    def wrap():
        print(f"function {func.__name__} is blocked")
    return wrap



class Gyumolcs:
    number: int
    def __init__(self, alma, banan):
        self.alma = alma
        self.banan = banan
        Gyumolcs.number += 1


    def increase_alma(self):
        self.alma += 1

    @staticmethod
    def number_of_gyumolcs():
        Gyumolcs.number += 1

@block
def printalma():
    print("alma")


printalma()
