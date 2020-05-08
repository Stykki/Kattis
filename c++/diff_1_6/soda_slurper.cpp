#include<iostream>

using namespace std;

int main()
{
    int owned;
    int found;
    int cost;
    int cans;
    int mep;
    std::cin >> owned;
    std::cin >> found;
    std::cin >> cost;
    cans = owned + found;
    int sodas = 0;
    while (cans >= cost)
    {
	sodas += cans / cost;
	mep = cans / cost;
	mep += cans % cost;
	cans = mep;

    }

    cout << sodas;

    return 0;
}
