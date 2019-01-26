from aiohttp import web


async def say(request):
    return web.json_response({'message': 'Hello World!'})
