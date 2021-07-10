#include <iostream>
using namespace std;

int main()
{
    int arr[6];
    for (int i = 0; i < 6; i++)
    {
        cin >> arr[i];
    }

    for (int i = 1; i < 6; i++)
    {
        int cur = arr[i];
        int j = i - 1;
        for (; arr[j] > cur && j >= 0; j--)
        {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = cur;
    }

    for (int i = 0; i < 6; i++)
    {
        cout << arr[i] << " ";
    }
}