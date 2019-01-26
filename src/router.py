from aiohttp import web


async def root(request: web.Request) -> web.Response:
    app = request.app
    response: dict = {}
    for name, resource in app.router.items():
        if 'formatter' in resource.get_info():
            path = resource.get_info()['formatter']
            n = name.replace('get-', '').replace('put-',
                                                 '').replace('post-', '').replace('delete-', '')

            if n not in response:
                response[n] = f'{path}'

    return web.json_response(response)


ROUTER = {
    "root": {
        "url": "/",
        "GET": "router.root"
    },
    "greeting": {
        "url": "/hello",
        "GET": "greeting.hello.say"
    }
}


def generate_routes() -> list:
    routes = []
    for key, value in ROUTER.items():

        if 'GET' in value:
            handler = value['GET']
            routes.append(
                web.get(value['url'], object_at_end_of_path(handler), name=f'get-{key}'))

        if 'PUT' in value:
            handler = value['PUT']
            routes.append(
                web.put(value['url'], object_at_end_of_path(handler), name=f'put-{key}'))

        if 'POST' in value:
            handler = value['POST']
            routes.append(
                web.post(value['url'], object_at_end_of_path(handler), name=f'post-{key}'))

        if 'DELETE' in value:
            handler = value['DELETE']
            routes.append(web.delete(value['url'], object_at_end_of_path(
                handler), name=f'delete-{key}'))
    return routes


def object_at_end_of_path(path):
    """Attempt to return the Python object at the end of the dotted
    path by repeated imports and attribute access.
    """
    access_path = path.split('.')
    module = None
    for index in range(1, len(access_path)):
        try:
            module_name = '.'.join(access_path[:-index])
            module = __import__(module_name)
        except ImportError:
            continue
        else:
            for step in access_path[1:-1]:
                module = getattr(module, step)
            break
    if module:
        return getattr(module, access_path[-1])
    else:
        return globals()['__builtins__'][path]
