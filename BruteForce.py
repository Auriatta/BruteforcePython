from pynput import keyboard
from array import array


class BruteForceNumpad:
    password: array
    password_current_view_index: int

    def __init__(self, password_len: int, start_password: int(array)) -> None:

        if len(start_password) > 0:
            self.password = start_password
        else:
            if password_len < 0:
                print("ERROR: Password length need to be greater then 0")
                exit()
            else:
                self.password.append(password_len * [0])
        self.setup_keyboard_listener()

    def next_index(self):
        self.password_current_view_index += 1
        if self.password_current_view_index > len(self.password):
            self.password_current_view_index = 0

    def set_password_index_value(self, value):
        if self.password_current_view_index <= 9:
            self.password[self.password_current_view_index] = value

    def get_password_index_value(self):
        return self.password[self.password_current_view_index]

    def run(self):
        password_last_index = len(self.password) - 1
        while self.password[password_last_index] < 9:
            new_value = self.get_password_index_value() + 1
            self.set_password_index_value(new_value)
            self.next_index()

    def stop(self):
        pass

    exit_key_listener: keyboard.Listener

    def on_press_exit(self, key):
        if keyboard.Key.esc == key:
            print("Keyboard Exit")
            print("Last password: ", self.password)
            exit()

    def setup_keyboard_listener(self):
        self.exit_key_listener = keyboard.Listener()
