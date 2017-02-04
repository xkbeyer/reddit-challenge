# https://www.reddit.com/r/dailyprogrammer/comments/5e4mde/20161121_challenge_293_easy_defusing_the_bomb/
# pylint: disable=C0111
# pylint: disable=missing-docstring

import sys
from enum import Enum

class CableColor(str, Enum):
    White = "white"
    Black = "black"
    Purple = "purple"
    Red = "red"
    Green = "green"
    Orange = "orange"

class State:
    def white(self, cable):
        not_allowed = [CableColor.White, CableColor.Black]
        if cable[0] in not_allowed:
            cable.clear()
        return
    def black(self, cable):
        not_allowed = [CableColor.White, CableColor.Green, CableColor.Orange]
        if cable[0] in not_allowed:
            cable.clear()
        return
    def red(self, cable):
        if cable[0] != CableColor.Green:
            cable.clear()
        return
    def orange(self, cable):
        must_do = [CableColor.Red, CableColor.Black]
        if cable[0] not in must_do:
            cable.clear()
        return
    def green(self, cable):
        must_do = [CableColor.White, CableColor.Orange]
        if cable[0] not in must_do:
            cable.clear()
        return
    def purple(self, cable):
        not_allowed = [CableColor.Purple, CableColor.Green, CableColor.Orange, CableColor.White]
        if cable[0] in not_allowed:
            cable.clear()
        return

def main():
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        lines = list(map(lambda s: s.strip(), lines))
        solver = State()
        while len(lines):
            cut_cable = getattr(solver, lines[0])
            del lines[0]
            if len(lines) == 0:
                print('Allrigth the bomb is defused.')
                return
            cut_cable(lines)
        print('Boom!')
        return

if __name__ == '__main__':
    main()
