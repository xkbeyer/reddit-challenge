# reddit challenge #290 Blinking LEDs 2016/11/02
# https://www.reddit.com/r/dailyprogrammer/comments/5as91q/20161102_challenge_290_intermediate_blinking_leds/
# input:
#  <line>: <whitespace> <instruction> |
#          <label>                    |
#          <empty>
#  
#  <instruction> : ld a,<num> |
#                  ld b,<num> |
#                  out (0),a  |
#                  rlca       |
#                  rrca       |
#                  djnz <labelref>
#  

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

def rlca(bits):
    return ((bits << 1) | ((bits & 0x80) >> 7)) &0xff

def rrca(bits):
    return ((bits >> 1) | ((bits & 0x01) << 7)) &0xff

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        i = 0
        loops = 0
        labels = {}
        while i < len(lines):
            line = lines[i]
            m = re.match(r'\s*ld\s+a\s*,\s*(\d{1,3})\s*', line)
            if m:
                a = int(m.group(1))
            m = re.match(r'\s*out\s+\(0\)\s*,\s*a\s*', line)
            if m:
                blinkLED(a)
            m = re.match(r'([a-z]+):\s*', line)
            if m:
                labels[m.group(1).strip()] = i
            m = re.match(r'\s+rlca\s*', line)
            if m:
                a = rlca(a)
            m = re.match(r'\s+rrca\s*', line)
            if m:
                a = rrca(a)
            m = re.match(r'\s+djnz\s+([a-z]*)\s*', line)
            if m:
                loops -= 1;
                if loops > 0 :
                    i = labels[m.group(1).strip()]
                else:
                    loops = 0
            m = re.match(r'\s*ld\s+b\s*,\s*(\d{1,3})\s*', line)
            if m:
                loops = int(m.group(1).strip())
            i += 1
