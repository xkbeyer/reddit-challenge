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

class Boom(Exception):
    def __init__(self):
        super(Boom, self).__init__("Boom")

class Defusing:
    def __init__(self, wiring_harness):
        self.cable = wiring_harness
    def white(self):
        not_allowed = [CableColor.White, CableColor.Black]
        if self.cable[0] in not_allowed:
            raise Boom()
        self.next()
        return
    def black(self):
        not_allowed = [CableColor.White, CableColor.Green, CableColor.Orange]
        if self.cable[0] in not_allowed:
            raise Boom()
        self.next()
        return
    def red(self):
        if self.cable[0] != CableColor.Green:
            raise Boom()
        self.next()
        return
    def orange(self):
        must_do = [CableColor.Red, CableColor.Black]
        if self.cable[0] not in must_do:
            raise Boom()
        self.next()
        return
    def green(self):
        must_do = [CableColor.White, CableColor.Orange]
        if self.cable[0] not in must_do:
            raise Boom()
        self.next()
        return
    def purple(self):
        not_allowed = [CableColor.Purple, CableColor.Green, CableColor.Orange, CableColor.White]
        if self.cable[0] in not_allowed:
            raise Boom()
        self.next()
        return
    def next(self):
        cut_cable = getattr(self, self.cable[0])
        del self.cable[0]
        if len(self.cable) == 0:
            print('Allrigth the bomb is defused.')
            return
        cut_cable()

def main():
    with open(sys.argv[1], 'r') as file:
        try:
            lines = list(map(lambda s: s.strip(), file.readlines()))
            solver = Defusing(lines)
            solver.next()
        except Boom as ex:
            print(ex)
        return

if __name__ == '__main__':
    main()
