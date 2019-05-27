#include<iostream>
using namespace std;
int main(){
    int x1,v1,x2,v2;
    cin>>x1>>v1>>x2>>v2;
    if(x1>x2 && v1>v2){
        cout<<"NO"<<"\n";
    }
    else if(x2>x1 && v2>v1){
        cout<<"NO"<<"\n";
    }
    else{
        int i=0,f=0;
        int d1=x1;
        int d2=x2;
        while(i<=100){
            d1=d1+v1;
            d2=d2+v2;
            if(d1==d2){
                f++;
                break;
            }
        }
        if(f==0){
            cout<<"NO"<<"\n";
        }
        else{
            cout<<"YES"<<"\n";
        }
    }
 return 0;   
}