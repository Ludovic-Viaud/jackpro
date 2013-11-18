from copy import copy
import random

class Sabot :
    def __init__(self, nb, cutcard) :
        self._cutcard = cutcard
        self._save = [x for x in range(2, 10)] + [10]*4 + [11]
        self._save *= 4*nb
        self.shuffle()

    def shuffle(self) :
        self._data = copy(self._save)
        random.shuffle(self._data)

    def cutcard(self) :
        return self._cutcard >= len(self._data)

    def draw(self) :
        return self._data.pop()

    def burn(self):
        self._data.pop()

    def cardsOut(self) :
        return len(self._save) - len(self._data)
