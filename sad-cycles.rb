# https://www.reddit.com/r/dailyprogrammer/comments/36cyxf/20150518_challenge_215_easy_sad_cycles/
puts "Sad Cycles"

puts "base:"
$b = gets.chomp.to_i
puts "number:"
number = gets.chomp

result = Array.new
doit = true
dbgmaxiter = 0

while doit do 

  numbers = number.split(//).map! {|s| s.to_i }

  sum = numbers.map {|n| n**$b}.reduce :+

  result << sum
  
  puts "#{result}->"
  maxi = result.length / 2
  (1..maxi).each { |i|
    a = result.last i
    b = result[result.length-i*2,i]
    c = a - b
    puts "#{i}:#{a}-#{b} = #{c}"
    if c.length == 0
      puts "sad cycle #{a}"
      doit = false
      break
    end
  }

  number = sum.to_s
  dbgmaxiter += 1
  if dbgmaxiter > 1000 then
    break
  end
end

puts "after #{dbgmaxiter}"
