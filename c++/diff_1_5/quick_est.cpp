#include<iostream>
#include<string>

using namespace std;

int main()
{
    int testAmt;
    cin >> testAmt;

    for (int i=1; i <= testAmt; i++)
    {
	string meme;
	cin >> meme;
	cout << meme.length() << "\n";
    }
}
