//Author - MANASSES KARIUKI = documentation
/*written on 4th of march 2024
    program to demonstrate basic structure of c++ program*/
#include<iostream>
//using std::cout or cin or endl
#define PI 3.1415

int r=2;
void area();

class MyClass
{
    public:
        int a;
        void display()
        {
            std::cout<<"inside class"<<std::endl;
        }
};
int main()
{
    MyClass m;
    m.a=90;
    m.display();
    area();
    std::cout<<"Hello world from main function!!"<<std::endl;
    std::cout<<m.a<<std::endl;
    return 0;
}


void area()
{
    float area;
    area=PI*r*r;
    std::cout<<area<<std::endl;
}
