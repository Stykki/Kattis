#include<iostream>

int main()
{
    int thickness = 4;
    int firstCut;
    int secondCut;
    
    int cakeLen;
    
    std::cin >> cakeLen;
    std::cin >> firstCut;
    std::cin >> secondCut;

    if ((cakeLen - firstCut) >= firstCut)
    {
	firstCut = cakeLen - firstCut;
    }

    if ((cakeLen - secondCut) >= secondCut)
    {
	secondCut = cakeLen - secondCut;
    }

    int awns = firstCut*secondCut*4;
    std::cout << awns;
    return 0;
}
