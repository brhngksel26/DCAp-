import pytest
from aiohttp import web
import asyncio
import inspect

def asyncio_run(async_func):

    def wrapper(*args, **kwargs):
        return asyncio.run(async_func(*args, **kwargs))
    
    wrapper.__signature__ = inspect.signature(async_func) 
    return wrapper



async def people(request):
    return web.Response(body=b"people")


def create_app():
    app = web.Application()
    app.router.add_route("GET", "/", people)
    return app


@asyncio_run
async def test_get_people_response(aiohttp_client):
    client = await aiohttp_client(create_app())
    resp = await client.get("/")
    assert resp.status == 200