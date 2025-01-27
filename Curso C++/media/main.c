#include <stdio.h>
#include <stdlib.h>

int main()
{
    float n1,n2,n3,n4,m;
    n1=n2=n3=n4=m = 0;

    printf("media");
    printf("nota1:\n");
    scanf("%f",&n1);
    printf("nota2:\n");
    scanf("%f",&n2);
    printf("nota3:\n");
    scanf("%f",&n3);
    printf("nota4:\n");
    scanf("%f",&n4);

    m = (n1+n2+n3+n4) / 4;

    printf("media %f\n\n",m);

    if(m >= 7){
        printf("aprovado\n\n");
    }else{
        printf("reprovado\n\n");
    }

    return 0 ;
}
