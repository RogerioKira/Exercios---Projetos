let valores = [8,1,7,4,3,9]
/*
console.log(valores[0])
console.log(valores[1])
console.log(valores[2])
console.log(valores[3])
console.log(valores[4])
console.log(valores[5])

for(let pos=0; pos <valores.length;pos++){
    console.log(`a posição de ${pos} tem valor ${valores[pos]}`)
}
*/

for(let pos in valores){
    console.log(`a posição de ${pos} tem valor ${valores[pos]}`)
}
