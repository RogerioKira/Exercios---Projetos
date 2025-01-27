#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{

    char c;
    printf("digite um minusculo:");
    scanf("%c", &c);

    if(c >= 'a')
    {
        printf("\n maiusculo: > %c < \n ", toupper(c));

        return 0;
    }

}
