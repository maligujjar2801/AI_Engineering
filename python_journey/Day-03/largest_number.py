n1 = float(input('Enter first number :'))
n2 = float(input('Enter second number :'))
n3 = float(input('Enter third number :'))
if n1 > n2 and n1 > n3 :
    print(f'{n1} is the largest number.')
elif n2 > n3 and n2 > n1 :
    print(f'{n2} is the largest number.')
else :
    print(f'{n3} is the largest number.')
