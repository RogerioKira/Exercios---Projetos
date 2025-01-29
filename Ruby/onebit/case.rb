puts "mes de nacimento numero"

month = gets.chomp.to_i

case month
when 1..3
    puts 'voce naceu no inicio'
when 9..12
    puts 'voce naceu no fim'
when 4..6
    puts 'voce naceu na primeira metade'
when 7..9
    puts 'segunda metade do ano'
else
    puts 'erro'
end
