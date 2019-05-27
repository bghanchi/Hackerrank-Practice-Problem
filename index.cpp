#include<iostream>
#include<vector>
using namespace std;
int main(){
    int p,index;
    cin>>p>>index;
    vector<int>a;
    for(int i=1;i<=3200;i++){
        a.push_back(i);
    }
    if(p>2){
        int j=1,kill=1;;
   for(int i=2;i<=p;i++){
        int k=i*i;
         j=1;
         while(k<=p){
             a[j*(k)]=0;
             j++;
         }
    }
    }

    for(int i=3;i<=p;i++){
        if(a[i]!=0){
            int f=0;
            for(int pr=2;pr<i;pr++){
                if(i%pr==0){
                    f++;
                    break;
                }
            }
            if(f==0){
                int j=1,kill=1;
                 int  k=i*i;
                while(k<=p){
                a[j*(k)]=0;
                j++;
                }
            }
        }
    }


    for(int i=1;i<=p;i++){
        cout<<a[i]<<"\n";
    }
     
     

 
}