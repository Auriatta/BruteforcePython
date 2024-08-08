from pynput import keyboard
from array import array


class BruteForceNumpad:
    password: array
    password_current_view_index: int

    def __init__(self, password_len: int) -> None:

        if password_len < 0:
             print("ERROR: Password length need to be greater then 0")
             exit()
        else:
            self.password = password_len * [0]
        self.password_current_view_index = 0
        print("Password Set:", self.password)

    def next_password_index(self):
        self.password_current_view_index += 1
        if self.password_current_view_index > len(self.password):
            self.password_current_view_index = 0

    def set_password_index_value(self, value):
        if self.password_current_view_index <= len(self.password):
            self.password[self.password_current_view_index] = value

    def get_password_index_value(self):
        return self.password[self.password_current_view_index]

    def run(self):
        self.generate_next_password()
        self.next_password_index()
        if self.password[len(self.password)-1] != 9:
            self.run()

    def generate_next_password(self):
        if self.password[self.password_current_view_index] < 10:
            self.password[self.password_current_view_index] = self.password + 1
            print("New Password:", self.password)




