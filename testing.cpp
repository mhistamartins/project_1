#include "project.h"
#include <vector>
#include <string>
#include <iostream>
using namespace std;
int main(void)
{
    cout << "Testing....." << std::endl;
    int i, n;
    string value;
    vector<string> VECT;
    cout << "Enter the elements in your vector..." << endl;
    for (int i = 0; i < sizeof(n); i++)
    {
        std::cin >> value;
        VECT.push_back(value);
    
    }
    for (int i = 0; i < n; i++)
    {
        cout << VECT[i] << " "<<endl;
    }
}