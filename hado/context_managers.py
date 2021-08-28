# -*- coding: utf-8 -*-

import asyncio

def _typing_done_callback(fut):
    # just retrieve any exception and call it a day
    try:
        fut.exception()
    except (asyncio.CancelledError, Exception):
        pass

class Typing:
    def __init__(self, messageable):
        self.loop = messageable._state.loop
        self.messageable = messageable

    async def do_typing(self):
        try:
            channel = self._channel
        except AttributeError:
            channel = await self.messageable._get_channel()

        typing = channel._state.http.send_typing

        while True:
            await typing(channel.id)
            await asyncio.sleep(5)

    def __enter__(self):
        self.task = asyncio.ensure_future(self.do_typing(), loop=self.loop)
        self.task.add_done_callback(_typing_done_callback)
        return self

    def __exit__(self, exc_type, exc, tb):
        self.task.cancel()

    async def __aenter__(self):
        self._channel = channel = await self.messageable._get_channel()
        await channel._state.http.send_typing(channel.id)
        return self.__enter__()

    async def __aexit__(self, exc_type, exc, tb):
        self.task.cancel()
