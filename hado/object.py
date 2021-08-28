# -*- coding: utf-8 -*-

from . import utils
from .mixins import Hashable

class Object(Hashable):
    """Represents a generic Discord object.

    The purpose of this class is to allow you to create 'miniature'
    versions of data classes if you want to pass in just an ID. Most functions
    that take in a specific data class with an ID can also take in this class
    as a substitute instead. Note that even though this is the case, not all
    objects (if any) actually inherit from this class.

    There are also some cases where some websocket events are received
    in :issue:`strange order <21>` and when such events happened you would
    receive this class rather than the actual data class. These cases are
    extremely rare.

    .. container:: operations

        .. describe:: x == y

            Checks if two objects are equal.

        .. describe:: x != y

            Checks if two objects are not equal.

        .. describe:: hash(x)

            Returns the object's hash.

    Attributes
    -----------
    id: :class:`int`
        The ID of the object.
    """

    def __init__(self, id):
        try:
            id = int(id)
        except ValueError:
            raise TypeError('id parameter must be convertable to int not {0.__class__!r}'.format(id)) from None
        else:
            self.id = id

    def __repr__(self):
        return '<Object id=%r>' % self.id

    @property
    def created_at(self):
        """:class:`datetime.datetime`: Returns the snowflake's creation time in UTC."""
        return utils.snowflake_time(self.id)
