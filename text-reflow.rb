# challenge https://www.reddit.com/r/dailyprogrammer/comments/4ybbcz/20160818_challenge_279_intermediate_text_reflow/

 
# justify algorithm according to
# http://www.rose-hulman.edu/Users/faculty/young/CS-Classes/csse220/200820/web/Programs/Markov/justification.html
def justify(line, width)
  sp = width - (line.length - 1)
  words = line.split(/ /)
  n = words.length - 1
  if sp == 0 then
    return line
  end
  ll = Array.new(n," ")
  if sp >= n then
    while sp > n
      ll.map!{|item| item + " "}
      sp -= n
    end
  end
  (1..sp).each { |i|
    pos = rand(n)
    ll[pos] += " "
  }
  return words.zip(ll).flatten.compact.join
end

text = 'In the beginning God created the heavens and the earth. Now the earth was
formless and empty, darkness was over the surface of the deep, and the Spirit of
God was hovering over the waters.

And God said, "Let there be light," and there was light. God saw that the light
was good, and he separated the light from the darkness. God called the light
"day," and the darkness he called "night." And there was evening, and there was
morning - the first day.'

pp = text.split(/\n\n/)
pp2 = pp.map{ |p| p.gsub(/[[:cntrl:]]/, ' ').rstrip }
pp2.each{ |p|
  words = p.split(/ /)
  nt = ""
  count = 0
  words.each{ |w|
    if (count + w.length) > 40
      nt << "\n"
      count = 0
    end
    nt << w << " "
    count += w.length + 1
  }
  nl = nt.split(/\n/)
  nl.each{ |l| puts justify(l, 40)}
  puts "\n"
}
