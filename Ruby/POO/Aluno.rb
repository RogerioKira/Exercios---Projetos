class Aluno
    @nome
    @idade

    def mudar_n(nome)
        @nome = nome
    end

    def mostar
        @nome
    end
end

a1 = Aluno.new

a1.mudar_n("d")

puts a1.mostar


