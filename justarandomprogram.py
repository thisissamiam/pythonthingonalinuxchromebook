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
layer = '1'
write('Hello!')
write('Welcome')
write('to...')
write('justarandomprogram!!!')
os.system('clear')
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
  layer = answer
elif answer == 'n':
  write('Ok, starting a new game')
else:
  exit()

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
        '1.3': {
        'intro': 'You scroll on your phone',
        'text': 'Do you get ready for school?',
        '1': 'No',
        '2': 'Yes',
    },
    '1.21': {
        'intro': "You decide that you don't want to go to school",
        'text': 'Play video games?',
        '1': 'No',
        '2': 'Yes',
    },
    '1.22': {
    'intro': 'You decide to go to school',
    'text': 'Where do you want to sit on the bus?',
    '1': 'Next to someone',
    '2': 'Alone',
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
    '1.112':{
    'intro': 'You go out the door pass a man, and start knocking on doors.',
    'text': 'You knock on someones door and they shove you and close the door. You are bleeding out. What do you do?',
    '1': 'Call for help',
    '2': 'Try to get up',
    '3': 'Stay there',
    },
    '1.1121':{
    'intro': 'You call for help and someone comes and calls 911.',
    'text': 'You do not survive in the hospital.',
    '1': 'Call for help',
    '2': 'Try to get up',
    '3': 'Stay there',
    '1.1113':{
        'intro': 'You look at the man. And punch them.',
        'text': 'The man takes their phone out runs away and calls the police. What do you do?',
        '1': 'Follow the man',
        '2': 'Run away',
        '3': 'Stay put',
    },
    '1.11131':{
        'intro': 'You follow the man.',
        'text': 'He goes inside his house. What do you do?',
        '1': 'Go inside his house',
        '2': 'Go to school',
    },
    '1.111311':{
        'intro': 'You follow him inside his house.',
        'text': 'The man was a murderer. What do you do?',
        '1': 'FIGHT BACK',
        '2': 'Give up',
    },
    '1.1113111':{
        'intro': 'You fight back.',
        'text': 'They kill you',
        '1': 'You died. This choice does not work',
    },
    '1.1113112':{
        'intro': 'You give up.',
        'text': 'They kill you even after you surrender',
        '1': 'You died. This choice does not work',
    },
    '1.111312':{
        'intro': 'You go to school normally.',
        'text': 'The police find you in school. What do you do?',
        '1': 'Hide',
        '2': 'Give up',
    },
    '1.1113121':{
    'intro': 'You hide from the police and they cannot find you.',
    'text': 'You were in the clear, but a kid sniched on you, and the police arrest you',
    '1': 'You got arrested. This choice does not work.',
    },
    '1.1113122':{
    'intro': 'You give up.',
    'text': 'The police arrest you.',
    '1': 'You were arrested. This choise does not work',
    },
    '1.11132':{
        'intro': 'You run away.',
        'text': 'Eventually, the police find you. What do you do?',
        '1': 'Evade',
        '2': 'Try to fight them',
    },
    '1.111321':{
        'intro': 'You attempt to run away from you.',
        'text': 'Eventually, the police catch up with you, and you trip and fall on a rock',
        '1': 'You died. This choice does not work',
    },
    '1.111322':{
        'intro': 'You fight the police.',
        'text': 'You lose the fight',
        '1': 'You died. This choice does not work',
    },
    '1.11133':{
        'intro': 'You stay put and let the police come.',
        'text': 'The police come and ask you what happend. What do you do?',
        '1': 'Lie',
        '2': 'Tell the truth',
      },
    '1.111331':{
        'intro': 'You lie to the police.',
        'text': "The police don't belive your lie and tell you to put your hands behind you back. What do you do?",
        '1': 'Try to resist',
        '2': 'Put your hands behind your back',
      },
    '1.1113312':{
        'intro': 'You tell the truth',
        'text': 'They arrest you. You are useless now.',
        '1': 'You got arrested. This choice does not work.'
      },
    '1.1113311':{
        'intro': 'You try to resist.',
        'text': 'They tase you and you fall onto the ground but you die',
        '1': 'You died. This choice does not work.'
      },
    '1.1113312':{
        'intro': 'You got arrested',
        'text': 'They arrest you and now you are useless in life',
        '1': 'You got arrested. This choice does not work.'
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

while True:
  try:
    if story.get(layer).get('intro'):
        write(story[layer]['intro'])
    write(story[layer]['text'])
    if story[layer].get('1'):
        write('1) ' + story[layer].get('1'))
    if story[layer].get('2'):
        write('2) ' + story[layer].get('2'))
    if story[layer].get('3'):
        write('3) ' + story[layer].get('3'))
  except:
    write('You finished the game as far as you could')
    exit()
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
  elif answer.lower() == 's':
    write('Saving game...')
    write(layer)
    write('The previous message is your save code')
    exit()
    
