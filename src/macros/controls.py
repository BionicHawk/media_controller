import pyautogui as pg

class Volume:

    @staticmethod
    def setVolumeUp():
        pg.press("volumeup")

    @staticmethod
    def setVolumeDown():
        pg.press("volumedown")
    
    @staticmethod
    def setVolume2Mute():
        pg.press("volumemute")


class AudioVideo:

    @staticmethod
    def togglePause():
        pg.press("playpause")

    @staticmethod
    def forward():
        pg.press("right")

    @staticmethod
    def rewind():
        pg.press("right")

    @staticmethod
    def nextTrack():
        pg.press("nexttrack")

    @staticmethod
    def previousTrack():
        pg.press("prevtrack")

    @staticmethod
    def toggleVideo2Fullscreen():
        pg.press("f")


class Navigation():

    @staticmethod
    def Enter():
        pg.press("enter")

    @staticmethod
    def nextItem():
        pg.press("tab")

    @staticmethod
    def previousItem():
        pg.hotkey("shift", "tab")


        