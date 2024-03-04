from fastapi import APIRouter
from ...macros.controls import AudioVideo

video_controller = APIRouter()

@video_controller.post('/playpause')
async def toggle_play_pause():
    AudioVideo.togglePause()
    return 'ok!'

@video_controller.post('/forward')
async def forward_video():
    AudioVideo.forward()
    return 'ok!'

@video_controller.post('/rewind')
async def rewind_video():
    AudioVideo.rewind()
    return 'ok!'

@video_controller.post('/next')
async def nextTrack():
    AudioVideo.nextTrack()
    return 'ok!'

@video_controller.post('/prev')
async def prev_track():
    AudioVideo.previousTrack()
    return 'ok!'

@video_controller.post('/fsn')
async def toggle_video_fullscreen():
    AudioVideo.toggleVideo2Fullscreen()
    return 'ok!';