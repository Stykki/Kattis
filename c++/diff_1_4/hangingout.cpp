#include<iostream>

int main()
{
    int fireShift;
    int cases;

    int terranceCount = 0;
    int rejectCount = 0;

    std::cin >> fireShift;
    std::cin >> cases;
    
    for (int i = 0; i <= cases; i++)
    {
	std::string entExt;
	int amt;

	std::cin >> entExt;
	std::cin >> amt;

	if (entExt == "enter")
	{
	    if ((amt + terranceCount) > fireShift)
	    {
		rejectCount++;
	    }
	    else
	    {
		terranceCount += amt;
	    }
	}
	else
	{
	    terranceCount -= amt;
	}

    }

    std::cout << rejectCount;

    return 0;


}
