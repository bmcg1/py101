score = input('Enter Score: ')
sc = float(score)
if sc > 1:
    print('Scores must be between 0 and 1!')
elif sc >= .9:
    grade = 'A'
    print(grade)
elif sc >= .8:
    grade = 'B'
    print(grade)
elif sc >= .7:
    grade = 'C'
    print(grade)
else:
    grade = 'F'
    print(grade)
