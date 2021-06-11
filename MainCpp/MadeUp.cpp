#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int retu;
    int gyou = 3;
    cin >> retu;

    vector<int> A(retu);
    vector<int> B(retu);
    vector<int> C(retu);

    for (int i = 0; i < retu; i++)
    {
        cin >> A(retu);
    }
    for (int i = 0; i < retu; i++)
    {
        cin >> B(retu);
    }
    

    cout << A(1) << endl;
    cout << B(1) << endl;

    // vector<vector<int>> inputGyouretu(retu,vector<int>(gyou));
    // for (int i = 0; i < retu; i++)
    // {
    //     for (int j = 0; j < gyou; j++)
    //     {
    //         cin >> inputGyouretu.at(i).at(j);
    //     }
    // }
    
    // cout << inputGyouretu.at(1).at(2) << endl;
}