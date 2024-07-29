from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key, Controller
from Timer import Timer
from asyncio import new_event_loop, set_event_loop, get_event_loop


async def timeout_callback():
    await asyncio.sleep(0.1)
    print('echo!')


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
    targets: set
    listener: Listener


    def __init__(self):
        self.__init_subclass__()
        self.mouse = Controller()


    def gather_targets(self):
        pass

    def on_click(self,x,y,button: Button,pressed):
        if button.left:
            self.targets.add((x,y))

    def clean_targets(self):
        self.targets.clear()

    def set_mode(self, mode: bool):
        self.mode = mode

    async def
    def run(self):
        if self.mode == 0: # collecting data
            self.listener = self.mouse.Listener(
                    on_click=self.on_click)
            self.listener.start()
        else:
            targets_iter = iter(self.targets)
            self.mouse.position = (next(targets_iter))
            self.mouse.press(Key.left)
            self.mouse.release(Key.left)
            timer = Timer(2,)
            loop = new_event_loop()
            set_event_loop(loop)
            try:
                loop.run_until_complete()
            finally:
                loop.run_until_complete(loop.shutdown_asyncgens())
                loop.close()







