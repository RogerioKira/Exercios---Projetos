#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("digite entre 0 e 9\n");
    int i ;
    scanf("%i", &i);

    switch(i){
    case 0:
        printf("zero");
        break;
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
    printf("entre 1 e 5");
    break;
    case 6:
        printf("seis");
        break;
    case 7:
    printf("sete");
    break;
    case 8:
        printf("oito");
        break;
    case 9:
    printf("nove");
    break;
     default:
    printf("meme");
    }

    return 0;
}
