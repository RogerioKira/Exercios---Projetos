#include <stdio.h>
#include <stdlib.h>

int main()
{
    float n1,n2,res ;
    char op = '0';

    do {


        n1 = n2 = res = 0;


        printf("(1)soma \n");
        printf("(2)sub \n");
        printf("(3) multi \n");
        printf("(4)div \n");
        printf("(0)sair \n");

        printf("informe operacao \n");
        printf("\t\t\t>>>");

        op = getchar();
        printf("\n");

        if(op != '0'){
        printf("digite numero\t\t\t>>>");
        scanf("%f", &n1);
        printf("digite numero\t\t\t>>>");
        scanf("%f", &n2);

        if(op == '1'){
            res = n1 + n2;
        }else{
            if(op == '2'){
                res = n1 - n2;
            }else{
                if(op == '3'){
            res = n1 * n2;
            }else{
                if(op == '4'){
                    res = n1 / n2;
                }
            }
        }
    }
}
                printf("\n resultado %f \n ", res);
                system("pause");
                system("cls");
}while(op !='0');
    return 0;
}
