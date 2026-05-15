import time
import random
import os

def write(input):
  print(input)
    # print()
    # total = ''
    # for i in input:
    #     total += i
    #     print(total)
    #     num = (random.randint(1,2))*.10
    #     time.sleep(num)
    #     print('\033[A\033[A')
    # print('')
    
# write('Hello!')
# write('Welcome')
# write('to...')
# write('justarandomprogram!!!')
# os.system('clear')
# write('Do you want the instructions? (y,n)')
# answer = input()
# if answer == 'y':
#     os.system('clear')
#     write('-----------------')
#     write('Instructions:')
#     write('You will be given a question.')
#     write('It will have multiple answer choices.')
#     write('You must say the number you want')
#     write('For example, 1, then hit enter')
#     write('Good luck!')
#     write('-----------------')
# # Check if the answer is not no
# elif answer != 'n':
#     write('You picked neither y or n!!')
#     # stop the program if the answer is not no
#     exit(0)
# # will only run if answer is no or when the instructions finish
# write('Do you have a save file to load from? (y,n)')
# answer = input()
# if answer == 'y':
#     write('Please paste your save code.')
#     answer = input()

story = {
    '1': {
        'text': 'You woke up from your bed. What do you do?',
        '1': 'Go back asleep',
        '2': 'Get up',
        '3': 'Scroll on your phone'
    },
    '1.1':{
        'intro': 'You go back to bed and sleep longer',
        'text': 'You woke up and noticed you have missed the bus. What do you do?',
        '1': 'Ask mom for a ride',
        '2': 'Walk to school',
        '3': 'Skip school'
    },
    '1.2': {
        'intro': 'You get out of bed and get ready for the bus',
        'text': 'Do you go to school?',
        '1': 'No',
        '2': 'Yes',
    },
    
    '1.11':{
        'intro': 'You get up and find mom. She sees you and yells at you that you missed the bus. You ask her for a ride.',
        'text': 'She says she has to go to work, and told you to figure it out yourself. What do you do?',
        '1': 'Walk to school',
        '2': 'Knock on other peoples doors untill one can give you a ride',
        '3': 'Skip school'
    },
    '1.111':{
        'intro': 'You grab your stuff and go out the door. You notice a man nearby.',
        'text': 'The man wanted to talk to you. What do you do?',
        '1': 'Talk to the man',
        '2': 'Tell them that you need to walk to school and you are late',
        '3': 'Punch them in the face'
    },
    '1.1111':{
        'intro': 'The man tells you that they have seen you before, and talks about life as he waters his plants.',
        'text': 'The man asks you if you could fill up his watering can. What do you do?',
        '1': 'Tell them you would love to but you really need to go',
        '2': 'Tell them sure, and help them fill up their watering can',
        '3': 'Take the watering can from them and throw it'
    },
    '1.11111':{
        'intro': 'The man said that was fine, and told you that they would be happy to see you later.',
        'text': 'You start walking to school, and look at your watch. You are 10 minutes late. What do you do?',
        '1': 'Start running to school',
        '2': 'Eat out at a fast food place',
        '3': 'keep walking how you were before'
    },
    '1.111111': {
        'intro': 'You start running to school as fast as you can.',
        'text': 'As you are running, your backpack is very heavy and is making it hard to run. What do you do?',
        '1': 'Take off the backpack and forget about it so you can run faster',
        '2': 'Accept you will be a little late and start walking',
        '3': 'Keep running as is'
    },
    '1.1111111': {
        'intro': 'You take off the backpack, throw it into a bush and keep running',
        'text': 'As you are running you need a drink. What do you do?',
        '1': 'Keep running to school',
        '2': 'Go back to the backpack and get your waterbottle',
        '3': 'Walk the rest'
    },
    '1.11111111': {
            'intro': 'You fought through the thirst and kept running',
            'text': 'You make it to school, but you are unsure of what to do next. What do you do?',
            '1': "Sneak in school so you aren't marked late",
            '2': 'Go in the main office to declare you are late',
    },
    '1.111111111': {
            'intro': 'You find your way in, but you run into a teacher.',
            'text': 'The teacher asks you are you late for school. What do you do?',
            '1': 'Tell them that you were late',
            '2': 'Ignore them and push them out of the way',
            '3': 'Lie and say you are not late'
    },
    '1.1111111111': {
        'intro': 'The teacher is accepting and marks you as on time, and you walk to your first class.',
        'text': 'You feel tired and want to take a nap, what do you do?',
        '1': 'Take the nap on your desk',
        '2': 'Sneak out after attendance so you can take a nap elsewhere',
        '3': "Pay attention and don't take a nap",
    },
    '1.11111111111': {
        'intro': 'The teacher notices and sends you to the office',
        'text': 'The principal asks you what happened. What do you say?',
        '1': 'You pull out a handbook, and act like you know everything in it, and say that it says that if a student has sleep deprivation, then you can nap',
        '2': 'Lie.',
        '3': 'IM SORRY IM SORRY IM SORRY *start crying*',
    },
    '1.111111111111': {
        'intro': 'The principal looks at you, and looks at the handbook.',
        'text': 'The principal agrees, and says they are sorry. What do you say?',
        '1': "Get Jiggy with it - trust i didn't make this - game dev?",
        '2': 'I KNEW IT HAAHAHAHHAHAHHA YOUR HANDBOOK SUCKS',
        '3': 'Tell them you accept their apology',
    }
    

    
}
layer = '1'
while True:
    try:
        write(story[layer]['intro'])
    except:
        pass
    write(story[layer]['text'])
    if story[layer].get('1'):
        write('1) ' + story[layer].get('1'))
    if story[layer].get('2'):
        write('2) ' + story[layer].get('2'))
    if story[layer].get('3'):
        write('3) ' + story[layer].get('3'))
    answer = input()
    if answer == '1':
        if '.' in layer:
            layer += '1'
        else:
            layer += '.1'
    elif answer == '2':
        if '.' in layer:
            layer += '2'
        else:
            layer += '.2'
    elif answer == '3':
        if '.' in layer:
            layer += '3'
        else:
            layer += '.3'



    #                                         if answer == '1':
    #                                             write('You picked: Take the nap on your desk')
    #                                             write('The teacher notices and sends you to the office')
    #                                             # PATH END
    # elif answer == '2':
    #     os.system('clear')
    #     write('You picked: Get up')
    #     write('You get ready for school, and head out for the bus')
    #     os.system('clear')
    #     write('The bus driver told you that you could sit anywhere that day. Where do you choose?')
    #     write('1) Sit with no one')
    #     write('2) Sit with people that look like they are nice')
    #     write('3) Sit with the person who is sitting alone')
    #     answer = input()
    #     if answer == '1':
    #         os.system('clear')
    #         write('You picked: Sit with no one')
    #         write('You found a spot where no one was and sat down')
    #         os.system('clear')
    #         write('You are not sure what to do on the bus, what should you do?')
    #         write('1) Take a nap')
    #         write('2) Look out the window')
    #         write('3) Scroll on your phone')
    #         answer = input()
    #         if answer == '1':
    #             os.system('clear')
    #             write('You picked: Take a nap')
    #             write('You fall asleep')
    #             os.system('clear')
    #             write('The bus made it to school, and someone woke you up. They looked nice. What do you do?')`
