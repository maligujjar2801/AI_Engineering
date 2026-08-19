a,b,c,d,e =int(input('Enter first number:')),int(input('Enter second number:')),int(input('Enter third number:')),int(input('Enter forth number:')),int(input('Enter fifth number:'))
sum = a+ b +c + d + e
print(f'The sum is {sum}.')
list=[]
list.append(a)
list.append(b)
list.append(c)
list.append(d)
list.append(e)
average = sum / len(list)
print(f'The average is {average}.')
