from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Models
from src.models.Control import Control
from src.models.Webpage import Webpage
from src.models.Position import Position
from src.models.Typed import Typed

import uvicorn
import webbrowser
import pyautogui
import time
import socket

pyautogui.FAILSAFE = False
app = FastAPI()

@app.get('/')
async def welcome():
    return 'Welcome to the server'

# controlador para abrir links en el navegador
@app.post('/open/web')
async def open_webpage(webpage: Webpage):
    if len(webpage.url) > 0:
        pyautogui.press('f11')
        print(f'[{webpage.fromUser}] is opening: {webpage.url}')
        pyautogui.hotkey('ctrl', 'w')
        webbrowser.open(webpage.url)
        time.sleep(4)
        pyautogui.press('f11')
        return 'ok!'
    raise HTTPException(400, detail='Some field or fields are empty')

# cambiar volumen
@app.post('/set/volume')
async def change_volume(control: Control):
    match control.command:
        case "up":
            pyautogui.press('volumeup')
            print(f"[{control.fromUser}] is setting the volume up")
            return 'ok!'
        case "down":
            pyautogui.press('volumedown')
            print(f"[{control.fromUser}] is setting the volume down")
            return 'ok!'
        case "mute":
            pyautogui.press('volumemute')
            print(f"[{control.fromUser}] is mutting the audio")
            return 'ok!'
    raise HTTPException(400, detail='Unknown command')

# controles de video
@app.post('/set/video')
async def video_controls(videoControl: Control):
    match videoControl.command:
        case "playpause":
            pyautogui.press('playpause')
            print(f"[{videoControl.fromUser}] is pausing or playing the media")
            return 'ok!'
        case "advance":
            pyautogui.press('right')
            print(f"[{videoControl.fromUser}] is advancing...")
            return 'ok!'
        case "goback":
            pyautogui.press('left')
            print(f"[{videoControl.fromUser}] is going back...")
            return 'ok!'
        case "next":
            pyautogui.press('nexttrack')
            print(f"[{videoControl.fromUser}] is skipping the next track")
            return 'ok!'
        case "prev":
            pyautogui.press('prevtrack')
            print(f"[{videoControl.fromUser}] is skipping the previous track")
            return 'ok!'
        case "enter":
            pyautogui.press('enter')
            print(f"[{videoControl.fromUser}] is doing enter")
            return 'ok!'
        case "lb":
            pyautogui.hotkey('shift', 'tab')
            print(f"[{videoControl.fromUser}] is using alt+tab")
            return 'ok!'
        case "rb":
            pyautogui.hotkey('tab')
            print(f"[{videoControl.fromUser}] is using tab")
            return 'ok!'
        case "fullscreen":
            pyautogui.press('f')
            print(f"[{videoControl.fromUser}] changed the view")
            return 'ok!'
    raise HTTPException(400, detail="Unknown command")

@app.post('/typing')
async def typying_on(typed: Typed):
    pyautogui.typewrite(message=typed.query)
    print(f"[{typed.fromUser}] typed")
    return 'ok!'

@app.post('/set/mouse')
async def move_mouse(pos: Position):
    pyautogui.displayMousePosition(pos.z, pos.y)
    return 'ok!'

if __name__ == '__main__':
    res = input("Would you like me to guess the hostname? (Y/N): ").lower()
    ip = '127.0.0.1'
    if res == 'y':
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
    else:
        ip = input("Give me the ip: ")

    uvicorn.run(app, host=ip, port=3001)
