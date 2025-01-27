#include <iostream>

using namespace std;

struct j{
    string titulo;
    int left;
    int top;

};

int main()
{
    j j1;
    j1.titulo = "Windows";
    j1.left = 0;
    j1.top = 0;

    j j2;
    j2.titulo = "Linux";
    j2.left = 250;
    j2.top = 250;

    cout << "titulo" + j2.titulo << endl
         << "left" << j2.left << endl
         << "top"  << j2.top << endl;

    return 0;
}
