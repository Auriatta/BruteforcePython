from BruteForce import BruteForceNumpad
from pynput import mouse
from array import array
from enum import Enum


class Modes(Enum):
    GATHER = 0
    PROCEED = 1


class BruteForceNumpadMouseInput(BruteForceNumpad):
    mode: bool
    mouse_controller: mouse.Controller
    mouse_listener: mouse.Listener
    click_targets_positions: array

    def __init__(self, password_len: int, start_password: int(array)):
        super().__init__(password_len, start_password)

        self.mouse_controller = mouse.Controller()
        self.mouse_listener = mouse.Listener(
            on_move=None,
            on_click=self.on_click,
            on_scroll=None)

    def add_target(self, x, y) -> bool:
        if len(self.click_targets_positions) >= len(self.password):
            return False

        self.click_targets_positions.append((x, y))
        print("Added new target [", len(self.click_targets_positions), "] at:", x, y)
        print("Waiting for num: ", (len(self.click_targets_positions) + 1))

        return True

    def on_click(self, x, y, button: mouse.Button, pressed):
        if button.left:
            self.mouse_listener.stop()
            success = self.add_target(x, y)
            if not success:
                self.set_mode(Modes.PROCEED)

    def set_mode(self, mode: Modes):
        self.mode = bool(mode)
        if mode == Modes.GATHER:
            print("Mode has been changed to: [GATHER]")
            self.mouse_listener.start()
        else:
            print("Mode has been changed to: [CRACK]")
            self.mouse_listener.stop()

    def input_password(self):
        for index in self.password:
            self.mouse_controller.position = self.click_targets_positions[index]
            self.mouse_controller.press(mouse.Button.left)

    def set_password_index_value(self, value):
        self.input_password()
        BruteForceNumpad.set_password_index_value(self, value)

    def run(self):
        self.set_mode(Modes.GATHER)
        print("Click at places in ascending order 0-9")
        print("Waiting for num: 0")
        while self.mode == Modes.GATHER:
            continue

        BruteForceNumpad.run(self)
