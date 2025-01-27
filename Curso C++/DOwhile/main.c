#include <stdio.h>
#include <stdlib.h>

int main()
{
    int cont = 0;
    char c;
    do {
        cont +=1;
        printf(" digite 0 \n");
        printf("%i quantia \n", cont);
        c = getchar();
    }

    while(c != '0');

    return 0;
}
