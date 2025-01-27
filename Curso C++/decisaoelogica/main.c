#include <stdio.h>
#include <stdlib.h>

int main()
{
   int i =10;

   printf("digite != de 5 : \n");
   scanf("%i", &i);

   if(i !=5)
    {
        printf("\n expresao:\n");
        printf("TRUE\n");
   }else{
       printf("\n expresao:\n");
       printf("FALSE\n");
   }

    return 0;
}
