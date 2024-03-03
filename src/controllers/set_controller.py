from fastapi import APIRouter, HTTPException
import pyautogui as pg

from ..macros.controls import AudioVideo, Navigation, Volume
from ..models.Control import Control
from ..models.Position import Position

set_controller = APIRouter()

# controles de volumen
@set_controller.post('/volume')
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
@set_controller.post('/video')
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

@set_controller.post('/set/mouse')
async def move_mouse(pos: Position):
    pg.displayMousePosition(pos.z, pos.y)
    return 'ok!'