#include<iostream>
#include<iomanip>
#include<limits>
using namespace std;

int main()
{
    float x=3456.123f;
    double a=9.123456789;
    long double aa=999.12345678L;
    //cout<<setprecision(17);
    cout<<cout.precision();
    //cout<<fixed<<"a="<<a<<endl;

    //cout<<setprecision(18);
    cout<<"\naa="<<aa<<endl;
    cout<<"x="<<x<<endl;
    cout<<"a="<<a<<endl;
    cout<<numeric_limits<float>::digits10<<endl;
    return 0;
}