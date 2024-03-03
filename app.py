from fastapi import FastAPI

# Controllers
from src.controllers.set_controller import set_controller
from src.controllers.open_controller import open_controller
from src.controllers.typing_controller import typing_controller

import uvicorn
import pyautogui
import socket

pyautogui.FAILSAFE = False
app = FastAPI()

app.include_router(router=set_controller, prefix='/set')
app.include_router(router=open_controller, prefix='/open')
app.include_router(router=typing_controller)

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
