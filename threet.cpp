#include<bits/stdc++.h>
using namespace std;
int main()
{
 long long n,m,a,ans,x,y;

 cin>>n>>m>>a;

 x = ((n+a)-1)/a;
 y = ((m+a)-1)/a;

 ans = x*y;

 cout<<ans<<endl;



    return 0;
}