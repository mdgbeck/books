import pyinputplus as pyip
import random, time

number_questions = 10
correct_answers = 0
tries = 3

for question_number in range(number_questions):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    prompt = '#%s:  %s * %s = ' % (question_number, x, y)

    try:
        #right answers handled by allowRegex, wrong with block
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (x * y)],
                blockRegexes=[('.*', 'Incorrect!')],
                timeout=3, limit=tries)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries')
    else:
        print('Correct!')
        correct_answers += 1
    time.sleep(.1)
print('Score: %s / %s' % (correct_answers, number_questions))


