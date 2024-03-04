from fastapi import APIRouter
import pyautogui

from ..models.Typed import Typed

typing_router = APIRouter()

@typing_router.post('/typing')
async def typing_on(typed: Typed):
    pyautogui.typewrite(message=typed.query)
    print(f"[{typed.fromUser}] typed")
    return 'ok!'