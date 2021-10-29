def vstolbik(y):
    for x in y :
        print(x )
english = {
    'лекцыи': 'not done',
    'duoling': 2,
}
pyhton = {
    'лекцыи': 1,
    'практика' : 1,
}
sport = {
    'зарядка' : 1,
    'go to gim' : 1,
}
a = str(1)
b = str(2)
c = str(3)
x =1
while x :
    x = input()
    if (x == a):
       print("sport:")
       vstolbik(sport.items())
    elif (x == b):
        print("pyhton")
        vstolbik(pyhton.items())
    elif (x == c):
        print("english")
        vstolbik(english.items())
    else:break



