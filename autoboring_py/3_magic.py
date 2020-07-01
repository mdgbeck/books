import random
def get_answer(ans_num):
    if ans_num == 2:
        return "It is certain"
    if ans_num == 3:
        return "It is decidedly so"
    if ans_num == 4:
        return "Yes"
    if ans_num == 5:
        return 'Reply hazy try again'
    if ans_num == 6:
        return 'Ask again later'
    if ans_num == 7:
        return 'Concentrate and ask again'
    if ans_num == 8:
        return 'Outlook not so good'
    if ans_num == 9:
        return 'Very doubtful loser.'
r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)
