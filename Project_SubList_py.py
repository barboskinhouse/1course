# Изменение изначального списка [0, ..., n]
# Первые k эл-тов преобразует в следующую комбинацию
def NextList(Lst, n, k):
    for i in range(k-1, 0-1, -1):
        if(Lst[i] < n - k + i):
            Lst[i] += 1
            for j in range(i+1, k):
                Lst[j] = Lst[j-1] + 1

            return True

    return False
                

# Создаёт промежуточный вложенный список
def Add(L, k):
    buf = []
    for i in range(k):
        buf.append(L[i])

    return buf

# Возвращает список с вложенными списками из комбинаций индексов
# всех возможных сочетаний из n по k,
# где k принимает значения от 0 до n
def index(n):
    L = [[]]   

    for i in range(1, n+1):
        L0 = [i for i in range(n)]
        k = i
        buf = Add(L0, k)
        L.append(buf)
        print(L0)
        if(n > k):
            while(NextList(L0, n, k)):
                buf = Add(L0, k)
                L.append(buf)
                print(L0)
                print(L)

    return L

# Составляет итоговый список сочетаний введённых эл-тов
def combination(L):
    comb = []
    for elem in L:
        buf = []
        for i in range(len(elem)):
            buf.append(s[elem[i]])
        if(not(buf in comb)):
            comb.append(buf)

    return comb


s = input('Введите эл-ты: ')
s = s.split()   
n = len(s)



Idx = index(n)
comb = combination(Idx)  

print(comb)



   
