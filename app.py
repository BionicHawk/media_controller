from fastapi import FastAPI, HTTPException

# Models
from src.models.Control import Control
from src.models.Webpage import Webpage
from src.models.Position import Position
from src.models.Typed import Typed

# Macros
from src.macros.controls import Volume
from src.macros.controls import AudioVideo
from src.macros.controls import Navigation

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
            Volume.setVolumeUp()
            return 'ok!'
        
        case "down":
            Volume.setVolumeDown()
            return 'ok!'
        
        case "mute":
            Volume.setVolume2Mute()
            return 'ok!'
        
    raise HTTPException(400, detail='Unknown command')

# controles de video
@app.post('/set/video')
async def video_controls(videoControl: Control):

    match videoControl.command:

        case "playpause":
            AudioVideo.togglePause()
            return 'ok!'
        
        case "advance":
            AudioVideo.forward()
            return 'ok!'
        
        case "goback":
            AudioVideo.rewind()
            return 'ok!'
        
        case "next":
            AudioVideo.nextTrack()
            return 'ok!'
        
        case "prev":
            AudioVideo.previousTrack()
            return 'ok!'
        
        case "enter":
            Navigation.Enter()
            return 'ok!'
        
        case "lb":
            Navigation.previousItem()
            return 'ok!'
        
        case "rb":
            Navigation.nextItem()
            return 'ok!'
        
        case "fullscreen":
            AudioVideo.toggleVideo2Fullscreen()
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
