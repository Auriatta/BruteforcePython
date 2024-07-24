from pynput import mouse, Controller
from enum import Enum

class MouseKeys(Enum):
    LMB = 1
    RMB = 2
    MMB = 3

class MouseHandling:
    mouse: Controller
    
    def __init__(self) -> None:
        mouse = Controller();    

    def get_mouse_position():

        pass
        
    def set_mouse_position(x:int, y:int):

        pass
        
    def press_mouse_key(mouse_key):

        pass
