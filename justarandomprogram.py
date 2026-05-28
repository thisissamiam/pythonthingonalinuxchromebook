import time
import random
import os
import yaml

# Player Defines
stats:{
"PlayerHealth": 20,
"PlayerAttack": 1,
"PlayerSoulPoint": 20,
"PlayerSpeed": 1,
"PlayerIntelligence": 10
}


def write(input):
    specialchar = False
    newline = False
    print()
    total = ''
    for i in input:
        if specialchar:
            if i == 'n':
                newline = True
            else:
                newline = False
        if i == '\\':
            specialchar = True
        else:
            specialchar = False
        if newline:
            print()
            total = ''
            newline = False
        if not specialchar and not newline:
            total += i
            print(total)
        num = (random.randint(0,1))*.10
        time.sleep(num)
        print('\033[A\033[A')
    print()
def userinput(string=''):
    return(input('>>> ' + string))
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
answer = userinput()
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
    answer = userinput()
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
    answer = userinput()
    if answer == 'y':
        write('Please paste your save code.')
        answer = userinput()
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


# GAME LOOP
while True:
    if level in data:
        node = data[level]
    else:
        write(f"Error: {level} does not exist in yaml")
        if loadedfromsave:
            write('Bad save file.')
        else:
            write('This probally means the game ended, but this should not happen in the release.')
        exit()
    if 'intro' in node:
        write(node['intro'])
        intro = True
    else:
        intro = False
    if 'introimage' in node:
        path = './Assets/'+ data[level]['introimage']+ '.txt'
        if os.path.isfile(path):
            with open(path, 'r') as file:
                print(file.read())
            time.sleep(2)
        else:
            write(f"{path} does not exist!!!")
    else:
        if intro:
            time.sleep(2)
    
    os.system('clear')
    if "stats" in node:
        for stat in node['stats']:
            amount = stat
            write(amount)
            exit()
            write('Your stat ' + stat + ' changed by ' + amount)
    write(node['text']) # write next question
    path = './Assets/' + data[level]['textimage'] + '.txt'
    if os.path.isfile(path):
        with open(path, 'r') as file:
            print(file.read())
            print()
    choices = data[level]['choices']
    for i in range(len(choices)):
        write(f"{str(i+1)}) {choices[i]['text']}")
    write(str((len(choices))+1) + ') Stats')
    answer = userinput()
    if not answer.isnumeric():
        if answer.lower() == 's':
            write('Saving game...')
            write(level)
            write('The previous message is your save code')
            exit()
        else:
            write("That's not a number!")
            continue
    answer = int(answer)
    if answer == len(choices) + 1:
        os.system('clear')
        write('Your stats are...')
        write(f'Health: {stats['PlayerHealth']}')
        write(f'Attack: {stats['PlayerAttack']}')
        write(f'PlayerSoulPoint: {stats[PlayerSoulPoint]}')
        write(f'Intelligence: {stats[PlayerIntelligence]}')
        write(f'PlayerSpeed: {stats[PlayerSpeed]}')
        print()
        write('Press enter to continue.')
        userinput()
    else:
        answer -= 1
        level = (choices[answer]['result'])
    os.system('clear')