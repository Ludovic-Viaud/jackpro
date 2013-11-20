import random

class Sabot :
    def __init__(self, nbDecks=6, cutcard=52) :
        self._cutcard = cutcard
        self._data = (list(range(2, 10)) + [10]*4 + [11]) * 4 * nbDecks
        self._current = len(self._data) - 1
        self.shuffle()

    def shuffle(self) :
        random.shuffle(self._data)
        self._current = len(self._data) - 1

    def cutcarded(self) :
        return self._current < self._cutcard

    def draw(self) :
        self._current -= 1
        return self._data[self._current+1]

    def decksOut(self) :
        return (len(self._data) - 1 - self._current) / 52

    def decksRem(self):
        return 6-self.decksOut()
