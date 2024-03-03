from fastapi import APIRouter
import pyautogui

from ..models.Typed import Typed

typing_controller = APIRouter()

@typing_controller.post('/typing')
async def typying_on(typed: Typed):
    pyautogui.typewrite(message=typed.query)
    print(f"[{typed.fromUser}] typed")
    return 'ok!'