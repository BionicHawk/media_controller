from fastapi import APIRouter

from ...macros.controls import Volume

audio_controller = APIRouter()

@audio_controller.post('/up')
async def volume_up():
    Volume.setVolumeUp()
    return 'ok!'

@audio_controller.post('/down')
async def volume_down():
    Volume.setVolumeDown()
    return 'ok!'

@audio_controller.post('/mute')
async def volume_mute():
    Volume.setVolume2Mute()
    return 'ok!'
