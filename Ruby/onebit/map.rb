array = [ 1,2,3,4]

puts "\n Executando .map multiplicando cada item por 2"

new_array = array.map do |a|
    a * 2
end 

puts "\n Array original"
puts "#{array}"

puts "\n novo array "
puts "#{new_array}"

puts "\n executando .map! multiplicando cada por 2"

array.map! do |a|
    a * 2
end

puts "\n array original"
puts " #{new_array}"
puts ''