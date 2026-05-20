import time
import random
import os
import yaml

# Player Defines
PlayerHealth = 20
PlayerAttack = 1
PlayerSpeed = 1
PlayerAccuracy = 10
PlayerEvasion = 0

def write(input):
    print()
    total = ''
    for i in input:
        total += i
        print(total)
        num = (random.randint(0,1))*.10
        time.sleep(num)
        print('\033[A\033[A')
    print('')
layer = '1'
os.system('clear')
write('Hello!')
write('Welcome')
write('to...')
write('justarandomprogram!!!')
time.sleep(1)
os.system('clear')
write('A image will appear on your screen. Please make sure it fits. Please say, "good" to confirm.')
size = ''
print(r'''
██████████████████████████████████████████████████████████████████████████████
█                                                                            █
█                                                                            █
█                                                                            █
█                                                                            █
█                                                                            █
█                                                                            █
█                                                                            █
█                                                                            █
█                                                                            █
█                                                                            █
█                                                                            █
█                                                                            █
█                                                                            █
█                                                                            █
██████████████████████████████████████████████████████████████████████████████''')
skip = False
loadedfromsave = False # avoid not defined error
level = 'WakeUp' # need to put it anywhere before save and must run so it doesn't get overwriten
answer = input()
if answer.lower() == 'good':
  write('Perfect')
  time.sleep(1)
  os.system('clear')
elif answer.lower() == 'skip': # easy dev way to skip instructions
    skip = True
else:
  write("You didn't follow the instructions. They may be cut off your screen. Try resizing your output/terminal")
  exit()
if not skip:
    write('Do you want the instructions? (y,n)')
    answer = input()
    if answer == 'y':
        os.system('clear')
        write('-----------------')
        write('Instructions:')
        write('You will be given a question.')
        write('It will have multiple answer choices.')
        write('You must say the number you want')
        write('For example, 1, then hit enter')
        write('To save the game, type S instead of a choice')
        write('Good luck!')
        write('-----------------')
    # Check if the answer is not no
    elif answer != 'n':
        write('You picked neither y or n!!')
        # stop the program if the answer is not no
        exit(0)
    # will only run if answer is no or when the instructions finish
    write('Do you have a save file to load from? (y,n)')
    answer = input()
    if answer == 'y':
        write('Please paste your save code.')
        answer = input()
        level = answer
        loadedfromsave = True
    elif answer == 'n':
        write('Ok, starting a new game')
        time.sleep(1)
        os.system('clear')
    else:
        exit()
with open('./Data/start.yaml', 'r') as file:
        data = yaml.safe_load(file)
while True:
    try:
        data[level]
    except:
        write(f"Error: {level} does not exist in yaml")
        if loadedfromsave:
            write('Bad save file.')
        else:
            write('This probally means the game ended, but this should not happen in the release.')
        exit()
    try:
        write(data[level]['intro'])
        intro = True
    except:
        intro = False
    try:
        with open('./Assets/'+ data[level]['introimage']+ '.txt', 'r') as file:
            print(file.read())
        time.sleep(2)
    except:
        if intro:
            time.sleep(2)
    os.system('clear')
    write(data[level]['text'])
    try:
        with open('./Assets/' + data[level]['textimage'] + '.txt', 'r') as file:
            print(file.read())
            print()
    except:
        pass
    choices = data[level]['choices']
    for i in range(len(choices)):
        print(f"{str(i+1)}) {choices[i]['text']}")
    print(str((len(choices))+1) + ') Stats')
    answer = input()
    try:
            answer = int(answer)
            if answer == len(choices) + 1:
                write('Your stats are...')
                write(f'Health: {PlayerHealth}')
                write(f'Attack {PlayerAttack}')
                write(f'Speed {PlayerSpeed}')
                write(f'Accuracy {PlayerAccuracy}')
                write(f'Evasion  {PlayerEvasion}')
                print()
                write('Press enter to continue.')
                input()
            else:
                answer -= 1
                level = (choices[answer]['result'])
    except:
        if answer.lower() == 's':
            write('Saving game...')
            write(level)
            write('The previous message is your save code')
            exit()
        else:
            write("That's not a number!")
            exit(1)
    os.system('clear')