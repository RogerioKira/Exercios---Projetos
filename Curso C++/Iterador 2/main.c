#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x = 0;
    int valD =0;

    printf("informe x \n");
    scanf("%i", &valD);

    while(x<valD){
        printf("%i\n", x * 10);
        x = x + 1;
    }
    return 0;
}
