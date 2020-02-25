from channels.generic.http import AsyncHttpConsumer
import asyncio
import time

class BasicHttpConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        await asyncio.sleep(4)
        await self.send_response(200, b"async piss of", headers=[
            (b"Content-Type", b"text/plain"),
        ]
    )

class BadHttpConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        time.sleep(4)
        await self.send_response(200, b"piss of", headers=[
            (b"Content-Type", b"text/plain"),
        ]
    )