from math import ceil, sqrt
s = input().strip()
c = ceil(sqrt(len(s)))
s=s.replace(" ","")
print(s)
print(c)
print(' '.join(map(lambda x: s[x::c], range(c))))


'''
import sys
from math import ceil, sqrt

s=input().strip()
s=s.replace(" ","")
exec("print(' '.join(map(lambda x: s[x::{0}], range({0}))))".format(ceil(sqrt(len(s)))))

'''
'''
import sys
from math import ceil, sqrt


s = input().strip()
c = ceil(sqrt(len(s)))
s=s.replace(" ","")
print(s)
print(c)
print(' '.join(map(lambda x: s[x::c], range(c))))
'''
'''
import sys
from math import ceil, sqrt

s=input().strip()
exec("print(' '.join(map(lambda x: s[x::{0}], range({0}))))".format(ceil(sqrt(len(s)))))
'''

'''
from math import ceil, sqrt

(lambda s: exec("print(' '.join(map(lambda x: \"{1}\"[x::{0}], range({0}))))".format(ceil(sqrt(len(s))),s)))(input().strip())
'''
'''
(lambda s:
  (lambda r:
      print(
        ' '.join(
                map(
                    lambda x: s[x::r],
                    range(r)
                   )
                )
           )
  )
     ( int(-(-(len(s)**0.5)//1)) )
) 
   ( input().strip() )
'''

'''
cin >> s;

auto n = s.size();
int row, column;

row = = round(sqrt(n));

if( row >= sqrt(n) )
    column = row; else column = row + 1;

for( int j = 0; j < column; j++ )
{
    for( int i = j; i < n; i += column )
        cout << s[i];

    cout << ' ';
}
'''