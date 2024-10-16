import math
from collections import *


def check_for_palindrome(string):
    lover_case_string_without_spaces = string.lower().replace(" ", "")
    queue = deque()
    for symbol in lover_case_string_without_spaces:
        queue.append(symbol)
    is_palindrome = True
    for i in range(0, math.floor(len(queue)/2)):
        if queue.pop() != queue.popleft():
            is_palindrome = False

    return is_palindrome


def main():
    print(check_for_palindrome("test"))
    print(check_for_palindrome("Lol"))
    print(check_for_palindrome("Abba"))
    print(check_for_palindrome("A b ba"))


main()
