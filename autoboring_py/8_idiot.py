import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

print('Thank you have a nice day.')

