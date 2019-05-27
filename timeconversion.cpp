#include<iostream>
#include<string>
#include <sstream>
using namespace std;
int main(){
    string s,s1,s2;
     cin>>s;
    
     s1=s.substr(s.length()-2,s.length());
     if(s1.compare("pm")==0 || s1.compare("PM")==0){
    
     s2=s.substr(0,2);

// string to number    
    stringstream geek(s2);
    int x = 0;
    geek >> x;
    x=12+x;
// numner to string   
    ostringstream str1;
    str1 << x;
    string geek1 = str1.str();
    
    
// replace string    
     s.replace(0,2,geek1);
     s=s.substr(0,s.length()-2);
     cout<<s<<"\n";
     }
    
    
     else{
     s2=s.substr(0,2);

// string to number    
    stringstream geek(s2);
    int x = 0;
    geek >> x;
      if(x==12){
         string str="00";        
     s.replace(0,2,str);
     s=s.substr(0,s.length()-2);
     cout<<s<<"\n";

      }
      else{
          s=s.substr(0,s.length()-2);
           cout<<s<<"\n";
       }
  
     }
return 0;
}


/*
     cout<<s1<<"\n";
    stringstream geek(s1);
    int x = 0;
    geek >> x;
    x=24-x;
    cout<<x<<"\n";

*/