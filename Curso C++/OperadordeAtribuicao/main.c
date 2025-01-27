#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x = 0;
    while(x<11){
        printf("msg\n");
        x +=1;
    }

    int i = 50;
    printf("soma %i\n" , i+=100);
    printf("sub %i\n" , i-=100);
    printf("multi %i\n" , i*=3);
    printf("div %i\n" , i/3);
    printf("res %i\n" , i/=3);

    return 0;
}
