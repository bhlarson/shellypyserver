#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};
    vector<int> nums {43, 26, 31415, 271828};

    int nums_array[] = {43, 26, 31415, 271828};

    cout << nums_array[0] << endl;

    for (const string& word : msg)
    {
        cout << word << " ";
    }

    cout << endl;

    for (const int& num : nums)
    {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}