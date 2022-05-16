print('Разделение списка на подсписки: ')
print('Из поданной строки цифр создается список, ')
print('содержащий подмножества введенного множества', end='\n'*2)

print('Введите строку, элементы разделяются пробелом: ')
s = input('s >>> ')
str_list = s.split()
print(str_list)
print()

sublist_s=[[]] # заготовка уже содержит пустой список
for x in str_list: # идем по элементам исходного списка
    print(sublist_s) 
    for i in range(len(sublist_s)): # по эл-там из списка найденных подмн-в
        billet = sublist_s[i].copy() # взяли эл-т (комбин-ю)
        billet.append(x) # добавили к найден-му до этого подм-ву текущий эл-т
        sublist_s.append(billet) # добавили состав-ю комбин-ю в список подмн-в
print()

sublist_s = sorted(sublist_s, key = len) # сортируем список по длине подмножеств
print(sublist_s)
