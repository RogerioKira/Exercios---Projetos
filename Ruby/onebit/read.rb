puts '--lista--'

file = File.open('lista.txt')

file.each do |line|
    puts line
end
