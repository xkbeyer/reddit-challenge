# reddit challenge #290 Blinking LEDs 2016/11/02
# input
#  ld a,14
#  out (0),a
#  ld a,12
#  out (0),a
#  ld a,8
#  out (0),a
#
#  out (0),a
#  ld a,12
#  out (0),a
#  ld a,14
#  out (0),a
# output
#  ....***.
#  ....**..
#  ....*...
#  ....*...
#  ....**..
#  ....***.

import sys
import re

def blinkLED(bits):
    outs = ""
    for i in range(7):
        if (1<<i) & bits:
            outs += "*"
        else:
            outs +="-"
    print(outs[::-1])
    return

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = re.match(r'\s?ld\s+a\s*,\s*(\d{1,3})', line.strip())
            if m:
                a = m.group(1)
            m = re.match(r'\s?out\s+\(0\)\s*,\s*a', line.strip())
            if m:
                blinkLED(int(a))
