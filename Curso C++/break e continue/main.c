#include <stdio.h>
#include <stdlib.h>

int main()
{
    for(int x =0; x<= 100;++x){
        if(x == 2){
                printf("-\n",x);
            continue;
        }
        if(x == 8){
            printf("-\n",x);
            break;
        }
        printf("%i \n", x);
    }
    return 0;
}
