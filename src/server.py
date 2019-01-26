import asyncio

from aiohttp import web

from router import generate_routes
from conf import settings


async def create_app():
    app = web.Application()
    app.router.add_routes(generate_routes())
    return app


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(create_app())
    web.run_app(app, host=settings['APP']['HOST'],
                port=settings['APP']['PORT'])
