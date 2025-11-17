x = int(input())
y = int(input())
z = input()

if z=='+' or z=='-' or z=='*' or z=='/':
    if z=='+':
        print(x+y)
    elif z=='-':
        print(x-y)
    elif z=='*':
        print(x*y)
    elif z=='/':
        if y==0:
            print('На ноль делить нельзя!')
        else:
            print(x/y)
else:
    print('Неверная операция')