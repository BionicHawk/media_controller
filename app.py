from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
import sys

# Controllers
from src.routers.set_router import set_router
from src.routers.open_router import open_router
from src.routers.typing_router import typing_router

import uvicorn
import socket

app = FastAPI()
root = os.path.dirname(os.path.abspath(__file__))

# middlewares
app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(router=set_router, prefix='/set')
app.include_router(router=open_router, prefix='/open')
app.include_router(router=typing_router)

@app.get('/', response_class=HTMLResponse)
async def welcome():
    return """
    <script>open('/static/index.html', '_self');</script>
    """

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 3001
    args = sys.argv
    if len(args) > 2:
        ip = args[1]
        port = int(args[2])

    uvicorn.run(app, host=ip, port=port)
