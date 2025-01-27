#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num1,num2,so,su,m,d;

    printf("calculadora\n");
    printf("dois numeros:  ");
    scanf("%i%i", &num1, &num2);

    so = num1 + num2;
    su = num1 - num2;
    m = num1 * num2;
    d = num1 / num2;

    printf("soma %i\n",so);
    printf("sub %i\n",su);
    printf("mul %i\n",m);
    printf("div %i\n",d);


    return 0;
}
