from BruteForce import BruteForceNumpad
from pynput import mouse
from pynput import keyboard
from array import array
from enum import Enum
import time
from sys import exit


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

        self.click_targets_positions = [(0, 0)]
        self.click_targets_positions.clear()
        self.mouse_controller = mouse.Controller()
        self.mouse_listener = mouse.Listener(
            on_move=None,
            on_click=self.on_click,
            on_scroll=None)
        self.keyboard_listener = keyboard.Listener(
            on_press=None,
            on_release=self.on_press_keyboard)

        self.set_mode(Modes.GATHER)

    def add_target(self, x, y) -> bool:
        self.click_targets_positions.append((x, y))
        print("Added new target [", len(self.click_targets_positions), "] at:", x, y)
        print("Waiting for number: ", (len(self.click_targets_positions)))
        if len(self.click_targets_positions) > 9:
            return False

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
            print("[press Up to start] or [press Down to exit] or ")
            print("Dont touch the mouse")
            self.keyboard_listener.start()

    def input_password(self):
        for index in self.password:
            self.mouse_controller.position = self.click_targets_positions[index]
            self.mouse_controller.press(mouse.Button.left)


    def run(self):
        print("Click at places in ascending order 0-9")
        print("Waiting for number: 0")
        while self.mode != Modes.GATHER:
            time.sleep(0.4)

    def generate_password(self):
        if self.terminate:
            return
        self.increase_current_password_by_index()
        self.next_password_index()
        self.input_password()
        if self.password[len(self.password)-1] != 9:
            self.generate_password()

    def on_press_keyboard(self, key):
        if keyboard.Key.down == key:
            print("Keyboard interrupt [EXIT]")
            print("Last generated password: ", self.password)
            exit()

        if keyboard.Key.up == key:
            if self.terminate:
                print("Generating [CONTINUE]")
                self.terminate = False
            else:
                print("Generating [START]")
            self.generate_password()

        if keyboard.Key.left == key:
            print("Generating [STOPPED]")
            self.terminate = True
