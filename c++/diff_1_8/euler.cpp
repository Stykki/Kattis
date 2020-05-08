#include<iostream>
#include<iomanip>



int main()
{
    int cool;
    std::cin >> cool;
    if (cool > 30) cool = 30;
    long double output = 1;
    double b = 1;
    for (int i = 1; i <= cool; i++)
    {
	b *= i;
	output += 1 / b;
    }
    std::cout << std::setprecision(15) << output;
    return 0;



}
