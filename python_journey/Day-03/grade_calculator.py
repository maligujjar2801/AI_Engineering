name = input('Enter your name:')
total = int(input('Enter total marks in all subjects :'))
math = int(input('Enter your marks in math :'))
computer = int(input('Enter your marks in computer:'))
physics = int(input('Enter your marks in physics:'))
obtained = math + physics + computer
percent = total / obtained * 100
if percent >= 90 :
    grade = 'A+'
    print(f'Hey {name}! You\'ve got a {grade} grade.')
elif percent >= 80 :
    grade = 'A'
    print(f'Hey {name}! You\'ve got a {grade} grade.')
elif percent >= 60:
    grade = 'B'
    print(f'Hey {name}! You\'ve got a {grade} grade.')
elif percent >= 40 :
    grade = 'C'
    print(f'Hey {name}! You\'ve got a {grade} grade.')
else :
    
    grade = 'F'
    print(f'Hey {name}! You\'ve got a {grade} grade.')
