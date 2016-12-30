# coding: utf-8
#uuencode challenge https://www.reddit.com/r/dailyprogrammer/comments/4xy6i1/20160816_challenge_279_easy_uuencoding/
#version 1
#Input: Text file given by first argument
#Output: Text file given by second argument

InputFileName = ARGV[0]
OutputFileName = ARGV[1]

text = Array.new
#text << "I feel very strongly about you doing duty. Would you give me a little more documentation about your reading in French? I am glad you are happy - but I never believe much in happiness. I never believe in misery either. Those are things you see on the stage or the screen or the printed pages, they never really happen to you in life."

File.open(InputFileName,"rb") do |input|
  while( line = input.gets )
    text << line
  end
end

outfile = File.open(OutputFileName, "w")

outfile.puts "begin 644 #{InputFileName}"
text.each { |textline|
  textline.scan(/.{1,45}/).each { |line|

    groups = line.unpack("B*")[0].scan(/.{6}/)

    numbers = groups.map{ |n| n.to_i(2) + 32 }
    newline = numbers.map{ |b| b.chr }.join()

    count = (line.length + 32).chr
    outfile.puts "#{count}#{newline}"
  }
}
outfile.puts "`\nend\n"
