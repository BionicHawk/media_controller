from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

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
    res = input("Would you like me to guess the hostname? (Y/N): ").lower()
    ip = '127.0.0.1'
    if res == 'y':
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
    else:
        ip = input("Give me the ip: ")

    uvicorn.run(app, host=ip, port=3001)
