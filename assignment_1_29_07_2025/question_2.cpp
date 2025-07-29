#include <bits/stdc++.h>
using namespace std;

int main()
{
  int n;
  cin >> n;
  vector<int>arr(n);
  for (int i =0 ; i < n; i++) cin >> arr[i];
  int avg = accumulate(arr.begin(), arr.end(), 0)/n;
  cout << avg << endl;
  return 0;
}
