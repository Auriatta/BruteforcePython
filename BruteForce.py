from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key, Controller
from array import array
from enum import Enum
import asyncio


async def timeout_callback():
    await asyncio.sleep(0.1)
    print('echo!')


class BruteForce:

    def __init__(self) -> None:
        pass

    def run(self):
        pass
        # brute force algorithm

    def stop(self):
        # stop brute force algorithm
        pass


class Modes(Enum):
    GATHER = 0
    PROCEED = 1


class BruteForceNumpadMouse(BruteForce):
    mode: bool
    mouse: Controller
    click_targets_positions: array
    listener: Listener
    pswd_len: int

    def __init__(self, pswd_len: int):
        super().__init__()
        self.pswd_len = pswd_len
        self.mouse = Controller()
        self.listener = Listener(
            on_move=None,
            on_click=self.on_click,
            on_scroll=None)

    def add_target(self, x, y) -> bool:
        if len(self.click_targets_positions) >= self.pswd_len:
            return False

        self.click_targets_positions.append((x, y))
        print("Added new target [", len(self.click_targets_positions), "] at:", x, y)
        print("Waiting for num: ", (len(self.click_targets_positions) + 1))

        return True

    def on_click(self, x, y, button: Button, pressed):
        if button.left:
            self.listener.stop()
            success = self.add_target(x, y)
            if not success:
                self.set_mode(Modes.PROCEED)

    def set_mode(self, mode: Modes):
        self.mode = bool(mode)
        if mode == Modes.GATHER:
            print("Mode has been changed to: [GATHER]")
            self.listener.start()
        else:
            print("Mode has been changed to: [CRACK]")
            self.listener.stop()

    async def crack(self, target_index):
        self.mouse.position = self.click_targets_positions[target_index]
        self.mouse.press(Key.left)
        await asyncio.sleep(0.1)

    async def confirm_keypad(self):
        self.confirm_keypad().send(Key.enter)
        pass

    def run(self):
        self.set_mode(Modes.GATHER)
        print("Click at places in ascending order 0-9")
        print("Waiting for num: 0")
        pass
