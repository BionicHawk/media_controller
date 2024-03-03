from fastapi import FastAPI

# Controllers
from routers.set_router import set_router
from routers.open_router import open_router
from routers.typing_router import typing_router

import uvicorn
import pyautogui
import socket

pyautogui.FAILSAFE = False
app = FastAPI()

app.include_router(router=set_router, prefix='/set')
app.include_router(router=open_router, prefix='/open')
app.include_router(router=typing_router)

@app.get('/')
async def welcome():
    return 'Welcome to the server'

if __name__ == '__main__':
    res = input("Would you like me to guess the hostname? (Y/N): ").lower()
    ip = '127.0.0.1'
    if res == 'y':
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
    else:
        ip = input("Give me the ip: ")

    uvicorn.run(app, host=ip, port=3001)
