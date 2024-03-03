from fastapi import APIRouter, HTTPException
import pyautogui as pg
import time
import webbrowser

from ..models.Webpage import Webpage

open_router = APIRouter()

@open_router.post("/web")
async def open_webpage(webpage: Webpage):

    if len(webpage.url) > 0:

        pg.press('f11')
        print(f'[{webpage.fromUser}] is opening: {webpage.url}')
        pg.hotkey('ctrl', 'w')
        webbrowser.open(webpage.url)
        time.sleep(4)
        pg.press('f11')
        return 'ok!'
    
    raise HTTPException(400, detail='Some field or fields are empty')
