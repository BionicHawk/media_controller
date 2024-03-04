from fastapi import APIRouter, HTTPException
import pyautogui as pg

from ..macros.controls import AudioVideo, Navigation
from ..models.Control import Control
from ..models.Position import Position

# Controllers
from .set_routers.audio_controller import audio_controller
from .set_routers.video_controller import video_controller
from .set_routers.navigation_controller import navigation_router

set_router = APIRouter()

set_router.include_router(router=audio_controller, prefix='/volume')
set_router.include_router(router=video_controller, prefix='/video')
set_router.include_router(router=navigation_router, prefix='/navigation')

# controles de volumen
# @set_router.post('/volume')
# async def change_volume(control: Control):

#     match control.command:

#         case "up":
#             Volume.setVolumeUp()
#             return 'ok!'
        
#         case "down":
#             Volume.setVolumeDown()
#             return 'ok!'
        
#         case "mute":
#             Volume.setVolume2Mute()
#             return 'ok!'
        
#     raise HTTPException(400, detail='Unknown command')

# controles de video
# @set_router.post('/navigation')
# async def video_controls(videoControl: Control):

#     match videoControl.command:

#         case "enter":
#             Navigation.Enter()
#             return 'ok!'
        
#         case "lb":
#             Navigation.previousItem()
#             return 'ok!'
        
#         case "rb":
#             Navigation.nextItem()
#             return 'ok!'
        
#         case "fullscreen":
#             AudioVideo.toggleVideo2Fullscreen()
#             return 'ok!'
        
#     raise HTTPException(400, detail="Unknown command")

@set_router.post('/set/mouse')
async def move_mouse(pos: Position):
    pg.displayMousePosition(pos.z, pos.y)
    return 'ok!'