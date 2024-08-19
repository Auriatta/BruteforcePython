import sys
from BruteForce import BruteForceDigitsGenerator
from pynput import mouse
from pynput import keyboard
from array import array
from enum import Enum
from time import sleep


class Modes(Enum):
    GATHER = 0
    PROCEED = 1


class BruteForceNumpadMouseInput(BruteForceDigitsGenerator):
    mode: bool
    mouse_controller: mouse.Controller
    mouse_listener: mouse.Listener
    keyboard_listener: keyboard.Listener
    click_targets_positions: array
    start_value: int

    def __init__(self, slots_amount: int):
        super().__init__(slots_amount)

        self.click_targets_positions = [(0, 0)]
        self.click_targets_positions.clear()
        self.mouse_controller = mouse.Controller()
        self.mouse_listener = mouse.Listener(
            on_move=None,
            on_click=self.on_click,
            on_scroll=None)
        self.keyboard_listener = keyboard.Listener(
            on_press=None,
            on_release=self.on_keyboard
        )

        self.set_mode(Modes.GATHER)

    def add_target(self, x, y) -> bool:
        self.click_targets_positions.append((x, y))
        print("Added new target [", len(self.click_targets_positions) - 1, "] at:", x, y)

        if len(self.click_targets_positions) > 9:
            return False

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
            print("[press Up to start] or [press Down to exit] or ")
            print("Dont touch the mouse")
            self.keyboard_listener.start()

    def input_password(self):
        for index in self.digits_slots:
            self.mouse_controller.position = self.click_targets_positions[index]
            sleep(0.09)
            self.mouse_controller.press(mouse.Button.left)
            sleep(0.01)
            self.mouse_controller.release(mouse.Button.left)

    def run(self, start_value: int = 0):
        self.start_value = start_value
        print("Click at places in ascending order 0-9")
        print("Waiting for number: 0")
        while self.mode != Modes.GATHER:
            sleep(0.4)

    def generate_next_digits(self, value: int = 0, recurrence: bool = True):
        if self.terminate:
            return

        if self.digits_slots[0] != 9:
            value = super().generate_next_digits(value, False)
            sleep(0.1)
            self.generate_next_digits(value, False)
        else:
            sys.exit(0)

    def on_keyboard(self, key):
        if keyboard.Key.down == key:
            print("Generating [STOPPED]")
            self.terminate = True

        if keyboard.Key.up == key:
            self.terminate = False
            print("Generating [START]")
            self.generate_next_digits(self.start_value)
