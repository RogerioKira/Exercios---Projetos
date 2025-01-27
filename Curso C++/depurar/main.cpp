#include <iostream>

using namespace std;

int main()
{
    cout << "digite entre 1 e 3" << endl;
    int num = 0;
    cin >> num;

    if(num==1){
        for(int i=0; i<5; i++){
            cout << "variavel for" << i << endl;
        }
    }else{
        if(num==2){
            int i2 = 0;
            while (i2<5){
                i2++;
                cout << "while" << i2 << endl;
            }
        }else{
            if(num==3){
                int i3 = 0;
                do {
                    i3++;
                    cout <<"valoer i3" << i3 << endl;
                }while(i3<50);
            }
        }
    }

    system("pause");
    return 0;
}
