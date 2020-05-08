#include<iostream>
#include<set>


using namespace std;

int main()
{
    std::set<int> the_int;

    for (int i = 0; i<=9;i++)
    {
	int number;
	std::cin >> number;
	the_int.insert(number%42);
    }
    int size = the_int.size(); 
    std::cout << size;

    return 0;
}
