a=input()


def reversed(str):
    a=list(str)
    a.reverse()
    str1=''
    for i in a:
        str1+=i

    return str1


string=reversed(a)
print(string)