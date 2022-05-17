'''
Разделение списка на подсписки
'''

st = input().split()
lst=[[]]
for i in range(1, len(st)+1):
    for j in range(len(st)-i+1):
        lst +=[st[j:j+i]]
one=list(st[0]+st[len(st)-1])
lst.append(one)
print(lst)

