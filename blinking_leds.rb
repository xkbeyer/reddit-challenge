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

def setLED(bits)
  outs = (0..7).map { |i|
    if ( (1<< i) & bits) > 0
      '*'
    else
      '-'
    end
  }.reverse.join
  puts "#{outs}"
end
  

regld = /\s?ld\s+a\,\s*(\d{1,3})/
regout= /\s?out\s+\(0\),\s*a/

InputFileName = ARGV[0]

text = Array.new
File.open(InputFileName,"rb") do |input|
  while( line = input.gets )
    text << line
  end
end

bits = nil
text.each { |line|
  m = line.match regld
  bits = m[1] if m
  if (line.match regout) != nil 
    setLED bits.to_i
  end
}
