// #include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
 
int main() {
    string input;
    cin >> input;
    reverse(input.begin(),input.end());
    for (int i = 0; i < input.size(); i++)
    {
        if(input.at(i) == '6'){
            input.at(i) = '9';
        }else if(input.at(i) == '9'){
            input.at(i) = '6';
        }else{
            continue;
        }
    }
    
    cout << input << endl;
}