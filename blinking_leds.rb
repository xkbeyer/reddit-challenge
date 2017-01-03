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

class Processor
  attr_accessor :line
  def initialize
    @line = 0
    @labels = Hash.new
    @bits = 0
    @loops = 0
  end
  def ld(register, value)
    if register == 'a'
      @bits = value.to_i
    elsif register == 'b'
      @loops = value.to_i
    else
      puts "Invalid register #{register}"
    end
    @line += 1
  end
  def out(port, value)
    puts "out #{port},#{value}" if $debug
    setLED
    @line += 1
  end
  def rlca(*ignore)
    puts "rlca" if $debug
    @line += 1
    @bits = ((@bits << 1) | ((@bits & 0x80) >> 7)) & 0xFF
  end
  def rrca(*ignore)
    puts "rrca" if $debug
    @line += 1
    @bits = ((@bits >> 1) | ((@bits & 0x01) << 7)) & 0xff
  end
  def djnz(label, *ignore)
    puts "dnjz #{label}" if $debug
    @loops -= 1
    if @loops > 0
      @line = @labels[label.strip] - 1
    else
      @loops = 0
    end
    @line += 1
  end
  def addLabel(label)
    puts "Add label '#{label}' at line #{@line}" if $debug
    @labels[label.strip] = @line;
    @line += 1
  end
  def setLED()
    outs = (0..7).map { |i|
      ((1<< i) & @bits) > 0 ? '*' : '.'
    }.reverse.join
    puts "#{outs}"
  end
  def nop
    @line += 1
  end
end

reg = /\s*(ld|out|rlca|rrca|djnz)\s*([a-z]+|a|b|\(0\))?(\s*,?\s*(\d{1,3}|a|b))?\s*/

InputFileName = ARGV[0]
text = File.open(InputFileName,"r").readlines()

vm = Processor.new
while vm.line < text.length do
  l = text[vm.line]
  m = (l.scan reg).flatten
  if m.count > 0 
    vm.method(m[0]).call(m[1],m[3])
  else
    m = (l.scan /([a-z]+):\s*/).flatten
    puts "#{l} #{m}" if $debug
    if m[0]
      vm.addLabel(m[0])
    else
      vm.nop
    end
  end
end

