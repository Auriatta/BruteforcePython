from pynput import keyboard
from array import array
from math import log10, floor


def count_digits(value: int):
    return floor(log10(value) + 1)


def get_single_digit(value, digit_position: int, digit_amount: int):
    lside_digit_sequence = floor(
        value / (10 ^ (digit_amount - (digit_amount - digit_position)))) * 10 ^ digit_position
    rside_digit_sequence = floor(value - lside_digit_sequence)
    return rside_digit_sequence / 10 ^ (digit_amount - digit_position)


class BruteForceNumpad:
    password: array
    password_current_view_index: int
    terminate: bool

    def __init__(self, password_len: int) -> None:

        if password_len < 0:
            print("ERROR: Password length need to be greater then 0")
            exit()
        else:
            self.password = password_len * [0]
        self.password_current_view_index = 0
        self.password_checked_number = 0
        self.terminate = False
        print("Password Set:", self.password)

    def next_password_index(self):
        if self.password_current_view_index > len(self.password) - 1:
            return False

        self.password_current_view_index += 1
        return True

    def set_password_index_value(self, value):
        if self.password_current_view_index <= len(self.password):
            self.password[self.password_current_view_index] = value

    def get_password_index_value(self):
        return self.password[self.password_current_view_index]

    def run(self):
        self.generate_password()

    def generate_password(self):
        if self.terminate:
            return

    def increase_current_password_by_index(self):
        if self.password[self.password_current_view_index] < 10:
            self.password[self.password_current_view_index] = self.password[self.password_current_view_index] + 1
            print("New Password:", self.password)
            return True
        else:
            return False
