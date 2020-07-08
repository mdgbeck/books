#! python3
# random_quiz.py Creates quizzes with questions and answers in random order

import random

dat = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacromento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'Saint Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New_Hampshire': 'Concord',
        'New_Jersey': 'Trenton',
        'New_Mexico': 'Sante Fe',
        'New_York': 'Albany',
        'North_Carolina': 'Raleigh',
        'North_Dakota': 'Bismark',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode_Island': 'Providence' ,
        'South_Carolina': 'Columbia',
        'South_Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Viginia': 'Richmond',
        'Washington': 'Olympia',
        'West_Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne',
} 

num_questions = 35

for quiz_num in range(num_questions):
    # Create the quiz and answer key files.
    quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w')
    answer_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w')
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form{quiz_num + 1})')
    quiz_file.write('\n\n')

    states = list(dat.keys())
    random.shuffle(states)

    for question_num in range(50):
        correct_answer = dat[states[question_num]]
        wrong_answers = list(dat.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}?\n')

        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. { answer_options[i]}\n")
        quiz_file.write('\n')

        answer_file.write(f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")
    quiz_file.close()
    answer_file.close()


