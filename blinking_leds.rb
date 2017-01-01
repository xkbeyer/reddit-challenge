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

def setLED(bits)
  outs = (0..7).map { |i|
    ((1<< i) & bits) > 0 ? '*' : '.'
  }.reverse.join
  puts "#{outs}"
end

def rlca(bits)
  ((bits << 1) | ((bits & 0x80) >> 7)) & 0xFF
end

def rrca(bits)
  ((bits >> 1) | ((bits & 0x01) << 7)) & 0xff
end

regld   = /\s?ld\s+a\,\s*(\d{1,3})/
regout  = /\s?out\s+\(0\),\s*a/
reglabel= /([a-z]+):\s*/
regrlca = /\s+rlca\s*/
regrrca = /\s+rrca\s*/
regloop = /\s+djnz\s+([a-z]*)\s*/
regldb  = /\s?ld\s+b\,\s*(\d{1,3})/

InputFileName = ARGV[0]
text = File.open(InputFileName,"r").readlines()

bits = nil
i = 0
labels = Hash.new
loops = 0

while i < text.length do
  m = text[i].match regld
  bits = m[1].to_i if m
  if (text[i].match regout) != nil 
    setLED bits
  end
  if (text[i].match regrlca) != nil
    bits = rlca(bits)
  end
  if (text[i].match regrrca) != nil
    bits = rrca(bits)
  end
  m = text[i].match reglabel
  if m != nil
    labels[m[1].strip] = i
  end
  m = text[i].match regloop
  if m != nil
    loops -= 1
    if loops > 0
      i = labels[m[1].strip] - 1
    else
      loops = 0
    end
  end
  m = text[i].match regldb
  if m != nil
    loops = m[1].to_i
  end
  i += 1
end

