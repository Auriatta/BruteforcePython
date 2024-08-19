import sys
from array import array
from math import log10, floor


def count_digits(value: int):
    return floor(log10(value) + 1)


def get_single_digit(value, digit_position: int, digit_amount: int):
    if digit_amount == 1:
        return value
    lside_digit_sequence = floor(value / (10**(digit_amount - digit_position)))
    rside_digit_sequence = value - lside_digit_sequence * 10**(digit_amount - digit_position)
    return floor(rside_digit_sequence / 10**((digit_amount - digit_position)-1))


class BruteForceDigitsGenerator:
    digits_slots: array
    digits_comb_max: int
    digits_slot_last_index: int
    terminate: bool

    def __init__(self, slots_amount: int) -> None:

        if slots_amount < 0:
            print("ERROR: Password length need to be greater then 0")
            sys.exit(0)
        else:
            self.digits_slots = slots_amount * [0]
        self.digits_comb_max = (10 ** slots_amount) - 1
        self.digits_slot_last_index = slots_amount - 1
        print("Password_MAX: ", self.digits_comb_max)
        self.terminate = False
        sys.setrecursionlimit(10 ** slots_amount)

    def run(self, start_value: int = 0):
        self.generate_next_digits(start_value)
        sys.exit(0)

    def generate_next_digits(self, value: int = 0, recurrence: bool = True):
        if self.terminate:
            return 0

        value += 1
        digit_amount = count_digits(value)
        if value > self.digits_comb_max:
            return 0

        self.transform_digits_value_to_slots(value, digit_amount)

        if recurrence:
            self.generate_next_digits(value)
        else:
            return value

    def transform_digits_value_to_slots(self, password_value, gen_digit_amount):
        for digit_index in range(0,gen_digit_amount):
            slot_index = self.digits_slot_last_index - (gen_digit_amount - digit_index) + 1
            self.digits_slots[slot_index] = get_single_digit(password_value, digit_index, gen_digit_amount)
