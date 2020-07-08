import pyinputplus as pyip
import random, time

number_questions = 2
correct_answers = 0
tries = 3

for question_number in range(number_questions):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    z = x * y
    prompt = '#%s:  %s * %s = ' % (question_number, x, y)
    
    i = 0
    while i < tries:
        answer = pyip.inputNum(prompt)
        if answer == z:
            print('Correct!')
            correct_answers +=1
            break
        print('Incorrect! %s tries remaining' % (tries - i-1))
        i += 1

print('You got %s right! That\'s %s' % (correct_answers, number_questions))
