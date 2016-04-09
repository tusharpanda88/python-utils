#pick items from shuffled list

import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)  # <1>
        random.shuffle(self._items)  # <2>

    def pick(self):  # <3>
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty shuff list')  # <4>

    def __call__(self):  # <5>
        return self.pick()


print BingoCage(range(3))
print BingoCage(range(3)).pick()
print BingoCage(range(3))
print callable(BingoCage)
