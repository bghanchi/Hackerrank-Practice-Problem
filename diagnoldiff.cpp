#include<iostream>
#include<vector>
using namespace std; 
void diagonalDifference(int *,int );
int main(){
    int n;
    cin>>n;
    vector<int>arr[n];
    for(int i=0;i<n;i++){
         for(int j=0;j<n;j++){
             int t;
             cin>>t;
             arr[i].push_back(t);
         }
    }
 int left=0,right=0,j=1;
 for(int i=0;i<n;i++){
     left+=arr[i][i];
     right+=arr[i][n-j];
     j++;
 }

 if(left-right<0){
     cout<<right-left<<"\n";
 }
 else{
     cout<<left-right<<"\n";
 }

return 0;    
}


/*

    for(int i=0;i<n;i++){
         for(int j=0;j<n;j++){
            cout<<arr[i][j]<<" ";
         }
         cout<<"\n";
    }


int main(){
     int n;
    cin>>n;
    int a[n][n];
    for( int i=1;i<=n;i++){
        for( int j=1;j<=n;j++){
            cin>>a[i][j];
        }
    }

      int diff;
     diagonalDifference(a[0],n);

  return 0;  
}

void  diagonalDifference(int *arr,int n) {
   cout<<arr[1][1]<<"\n";
}

*/