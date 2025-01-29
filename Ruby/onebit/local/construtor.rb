class Person

    def initialize (name,age)
        @name = name
        @age = age
    end

    def check
        puts "instacia iniciada"
        puts "name = #{@name}"
        puts "idade = #{@age}"
    end
end

person = Person.new('Jo',12)
person.check