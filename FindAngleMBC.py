import math
ab=int(input())
bc=int(input())
ac=math.sqrt(pow(ab,2)+pow(bc,2))
md=math.sqrt(pow(ac/2,2)-pow(bc/2,2))
angle=math.atan(md/(bc/2))
print(str(int(round((math.degrees(angle)))))+'°')


'''
import math 
AB = int(input()) 
BC = int(input())
print(math.atan2(AB,BC))
###print str(int(round(math.degrees(math.atan2(AB,BC)))))+'°'
'''
