var agora = new Date()
var diaS = agora.getDay()

console.log(diaS)

switch(diaS){
    case 0 :
        console.log ('domingo')
        break
     case 1 :
        console.log ('segunda')
        break    
    case 2 :
        console.log ('TERÇA')
        break
    case 3 :
        console.log ('quarta')
          break
    case 4 :
        console.log ('quinta')
        break
    case 5 :
        console.log ('sexta')
         break
     case 6 :
        console.log ('sabado')
         break
         default:
            console.log('invalido')
            break
        }