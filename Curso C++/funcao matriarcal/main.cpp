#include <iostream>

using namespace std;

int main()
{
    int p[10][10] ={};

    for(int x = 0; x < 10; x++){
        for(int y = 0; y<10;y++){
            p[x][y]= (3*(x + 1) + (y*y));

            string end = (y < 9) ? "," : "\n";
            cout << p[x][y] <<endl;
        }
    }

    return 0;
}
