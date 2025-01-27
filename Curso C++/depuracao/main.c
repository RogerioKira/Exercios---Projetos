#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("digite 1\n");
    char c;
    c = getchar();

    if (c == '1')
    {
        printf("\n correto \n");
    }else{
        printf("\n invalido \n");
        printf("digitou >%c< \n", c);
    }
    return 0;
}
