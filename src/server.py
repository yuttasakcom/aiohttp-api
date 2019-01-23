from aiohttp import web

from conf import settings


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/', handle), web.get('/{name}', handle)])

web.run_app(app, host=settings['APP']['HOST'], port=settings['APP']['PORT'])
