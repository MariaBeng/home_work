def funk(a,b): #task 2
    if a > b:
        print(a)
    if a < b :
        print(b)
funk(6,-400)


def funk1(c,d): #task 3
    if c - d == 135 or d -c == 135:
        print('yes')
    else:
        print('no')
funk1(1,137)


def funk2(e): #task 4
    if 1 <= e <= 3:
        print('Winter')
    elif 4 <= e <= 6:
        print('Spring')
    elif 7 <= e <= 9:
        print('Summer')
    elif 10 <= e <= 12:
        print('Fall')
    else:
        print('Choose 1 to 12')

funk2(2)


a = 20   #task 5
b = 136
c = 12

if a > 10 and b > 10 and c > 10:
    print('yes')

else:
    print('no')
