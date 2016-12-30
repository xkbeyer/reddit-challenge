require 'set'
dimension = gets.chomp.split(/ /).map{ |s| s.to_i }

sheets = Array.new
while line = gets
  sheets << line.chomp.split(/ /).map{ |s| s.to_i }
end

colors = SortedSet.new([0])

canvas = Array.new(dimension[1]) { Array.new(dimension[0],0) }
sheets.each { |sheet|
  color = sheet[0]
  colors << color
  xstart = sheet[1]
  ystart = sheet[2]
  xend = xstart + sheet[3] - 1
  yend = ystart + sheet[4] - 1
  (ystart..yend).each { |y| 
    (xstart..xend).each { |x|
      canvas[y][x] = color
    }
  }
}

colors.each{ |c|
  n = canvas.flatten.count(c)
  puts "#{c} #{n}"
}
