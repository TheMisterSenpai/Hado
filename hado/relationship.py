# -*- coding: utf-8 -*-

from .enums import RelationshipType, try_enum
from . import utils

class Relationship:
    """Represents a relationship in Discord.

    A relationship is like a friendship, a person who is blocked, etc.
    Only non-bot accounts can have relationships.

    .. deprecated:: 1.7

    Attributes
    -----------
    user: :class:`User`
        The user you have the relationship with.
    type: :class:`RelationshipType`
        The type of relationship you have.
    """

    __slots__ = ('type', 'user', '_state')

    def __init__(self, *, state, data):
        self._state = state
        self.type = try_enum(RelationshipType, data['type'])
        self.user = state.store_user(data['user'])

    def __repr__(self):
        return '<Relationship user={0.user!r} type={0.type!r}>'.format(self)

    @utils.deprecated()
    async def delete(self):
        """|coro|

        Deletes the relationship.

        .. deprecated:: 1.7

        Raises
        ------
        HTTPException
            Deleting the relationship failed.
        """

        await self._state.http.remove_relationship(self.user.id)

    @utils.deprecated()
    async def accept(self):
        """|coro|

        Accepts the relationship request. e.g. accepting a
        friend request.

        .. deprecated:: 1.7

        Raises
        -------
        HTTPException
            Accepting the relationship failed.
        """

        await self._state.http.add_relationship(self.user.id)
