from fastapi import APIRouter
from ...macros.controls import Slideshow, AudioVideo

slideshow_controller = APIRouter()

@slideshow_controller.post('/next')
async def next_slide():
    Slideshow.nextSlide()

@slideshow_controller.post('/prev')
async def prev_slide():
    Slideshow.prevSlide()

@slideshow_controller.post('/forward')
async def forward():
    AudioVideo.forward()

@slideshow_controller.post('/rewind')
async def rewind():
    AudioVideo.rewind()
    
@slideshow_controller.post('/switchmode')
async def switchMode():
    Slideshow.slideshowMode()