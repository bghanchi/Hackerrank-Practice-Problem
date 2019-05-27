h=int(input())
m=int(input())
hour=['','one','two','three', 'four', 'five', 'six','seven','eight', 'nine', 'ten','eleven','twelve']
minute=['','one','two','three', 'four', 'five', 'six','seven','eight', 'nine', 'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine']

if m<30 and m>0:
    if m==15:
        print('quarter past',hour[h]) 
    else:
        print(minute[m],'minutes past',hour[h]) 
elif m>30 and m<60:
    if m==45:
        print('quarter to',hour[h]) 
    else:
        print(minute[60-m],'minutes to',hour[h+1]) 
elif m==30:
    print('half past',hour[h])
else:
    print(hour[h],"o' clock")    

