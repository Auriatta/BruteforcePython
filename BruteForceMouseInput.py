from BruteForce import BruteForceNumpad
from pynput import mouse
from pynput import keyboard
from array import array
from enum import Enum
from asyncio import sleep
import time


class Modes(Enum):
    GATHER = 0
    PROCEED = 1


class BruteForceNumpadMouseInput(BruteForceNumpad):
    mode: bool
    mouse_controller: mouse.Controller
    mouse_listener: mouse.Listener
    keyboard_listener: keyboard.Listener
    click_targets_positions: array

    def __init__(self, password_len: int):
        super().__init__(password_len)
        self.click_targets_positions = [(0,0)]
        self.click_targets_positions.clear()
        self.mouse_controller = mouse.Controller()
        self.mouse_listener = mouse.Listener(
            on_move=None,
            on_click=self.on_click,
            on_scroll=None)
        self.keyboard_listener = keyboard.Listener(
            on_press=None,
            on_release=self.on_press_keyboard)


    def add_target(self, x, y) -> bool:
        if len(self.click_targets_positions) >= 10:
            return False

        self.click_targets_positions.append((x, y))
        print("Added new target [", len(self.click_targets_positions), "] at:", x, y)
        print("Waiting for number: ", (len(self.click_targets_positions)))

        return True

    def on_click(self, x, y, button: mouse.Button, pressed):
        if button == mouse.Button.left and pressed:
            success = self.add_target(x, y)
            if not success:
                self.set_mode(Modes.PROCEED)

    def set_mode(self, mode: Modes):
        self.mode = bool(mode)
        if mode == Modes.GATHER:
            print("Mode has been changed to: [GATHER]")
            self.mouse_listener.start()
        else:
            print("Mode has been changed to: [GENERATING CODE]")
            self.mouse_listener.stop()

    def input_password(self):
        for index in self.password:
            self.mouse_controller.position = self.click_targets_positions[index]
            self.mouse_controller.press(mouse.Button.left)
    
    def next_password_index(self):
        self.input_password()
        super().next_password_index()

    def run(self):
        self.set_mode(Modes.GATHER)
        print("Click at places in ascending order 0-9")
        print("Waiting for number: 0")
        while self.mode != Modes.GATHER:
            time.sleep(0.4)
        print("Data fulfilled waiting to start... [press Up to start] or [press Down to exit]")
        print("Dont touch the mouse")
        self.keyboard_listener.start()

    def on_press_keyboard(self, key):
        if keyboard.Key.down == key:
            print("Keyboard Exit")
            print("Last password: ", self.password)
            exit()

        if keyboard.Key.up == key:
            print("Generating started..")
            super().run()

