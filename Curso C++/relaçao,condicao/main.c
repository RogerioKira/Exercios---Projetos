#include <stdio.h>
#include <stdlib.h>

int main()
{
    int iJ,iI;
    iJ = 17;
    iI = 60;

    int idade = 0;

    printf("idade:\n");
    scanf("%i", &idade);

    if(idade<= iJ){
        printf("\n jovem \n");
    }else{
        if(idade >= iI){
            printf("\n idoso\n");
        }else{
            if((idade>iJ)&&(idade<iI)){
                printf("meia idade");
            }
        }
    }

    return 0;
}
