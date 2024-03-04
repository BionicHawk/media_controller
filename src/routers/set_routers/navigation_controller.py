from fastapi import APIRouter

from ...macros.controls import Navigation

navigation_router = APIRouter()

@navigation_router.post('/enter')
async def press_enter():
    Navigation.Enter()
    return 'ok!'

@navigation_router.post('/lb')
async def press_left_button():
    Navigation.nextItem()
    return 'ok!'

@navigation_router.post('/fullscreen')
async def press_left_button():
    Navigation.previousItem()
    return 'ok!'