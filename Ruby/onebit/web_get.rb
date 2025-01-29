require 'net/http'

example = Net::HTTP.get('example.com','/indez.html')

File.open('example.html', 'w') do |line|
    line.puts(example)
end
