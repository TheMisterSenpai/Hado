# -*- coding: utf-8 -*-

class EqualityComparable:
    __slots__ = ()

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.id == self.id

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return other.id != self.id
        return True

class Hashable(EqualityComparable):
    __slots__ = ()

    def __hash__(self):
        return self.id >> 22
