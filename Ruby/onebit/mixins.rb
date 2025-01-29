module ImpressaoDecorada
    def imprimir text
        decoracao = '#' * 100
        puts decoracao
        puts text
        puts decoracao
    end
end

module Pernas
include ImpressaoDecorada
    def chute_frontal
        imprimir 'chute frontal'
    end

    def chute_lateral
        imprimir 'chute lateral'
    end
end


module Bracos
include ImpressaoDecorada
    def jab_de_direira
        imprimir 'jab direita'
    end

    def jab_de_esquerda
        imprimir 'jab esqueda'
    end

    def gancho
        imprimirm'gancho'
    end
end

class LutadorX
    include Pernas
    include Bracos
end

class LutadorY
include Pernas
end

lutadorx = LutadorX.new
lutadorx.chute_frontal
lutadorx.jab_de_direira

lutadory = LutadorY.new
lutadory.chute_lateral