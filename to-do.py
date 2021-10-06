allthings=['создать список дел','делать уроки','учить англиский','читать книи','зделать зарядку','играть в комп','смотреть видосиики','получить пневмат']
businesstoday=['создать список дел','делать уроки','учить англиский','читать книи','зделать зарядку']
completedcases= ['играть в комп','смотреть видосиики']
casesinprogress=['получить пневмат']

x = input()
a = str(1)
b = str(2)
c = str(3)
d = str(4)
if (x==a):
    print('Все дела:')
    print(*allthings, sep=", ")
elif (x==b):
    print("Дела на сегодня:")
    print(*businesstoday, sep=", ")
elif (x==c):
    print("Выполненные дела:")
    print(*completedcases, sep=", ")
elif (x==d):
    print("Дела в процессе:")
    print(*casesinprogress, sep=", ")
else:
    allthings.append(x)



