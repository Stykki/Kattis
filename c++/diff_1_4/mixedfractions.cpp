#include<iostream>


int main()
{
    int num1;
    int num2;

    int x;
    int y;

    std::cin >> num1;
    std::cin >> num2;

    while ((num1 != 0) && (num2 != 0))
    {
	x = num1 / num2;
	y = num1 % num2;
	std::cout << x << " " << y << " / " << num2 << "\n";

	std::cin >> num1;
	std::cin >> num2;

    }

    return 0;



}
