require 'os'

def my_os
    if OS.windows?
        "windons"
    elsif OS.linux?
        "linux"
    elsif Os.mac?
        "Osx"
    else
        "nao"
    end
end

puts "meu pc #{OS.cpu_count} cores, e #{OS.bits} bits e o sistema e #{my_os}"