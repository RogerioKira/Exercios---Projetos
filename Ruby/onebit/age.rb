result = ''
loop do
puts result
puts 'selecione'
puts '1 - descobrir idade'
puts '0 - sair'
print'opcao:'

option=gets.chomp.to_i

if option == 1
    print 'digite ano nacimento'
    year_birth = gets.chomp.to_i
    print 'ano atual'
    current_year = gets.chomp.to_i
    age = current_year - year_birth
    result = "quem naceu em #{year_birth}, tem #{age} anos em #{current_year}"
elsif option == 0
    break if option == 0
else
    result = 'invalido'
end

system "clear"
end