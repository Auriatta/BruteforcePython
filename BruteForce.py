from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller


class BruteForce:
    pswd_len: int

    def __init__(self, pswd_len) -> None:
        self.pswd_len = pswd_len
        pass

    def run(self):
        pass
        # brute force algotithm

    def stop(self):
        # stop brute force algorithm
        pass


class BruteForceMouse(BruteForce):
    mode: bool
    mouse: Controller
    targets = {}


    def __init__(self):
        self.__init_subclass__()
        self.mouse = Controller()

    def gather_targets(self):
        pass

    def run(self):
        if self.mode == 0:
            pass
        else:
            pass




