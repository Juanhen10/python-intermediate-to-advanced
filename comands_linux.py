from os import system
from time import sleep

system('cls')


def line():
    a = '•'
    s = a * 50
    print(s)


def linha(text):
    s = ' '
    if text != len(s):
        s = '♦'
        a = s * len(text)
        print(a)
        print(text)
        print(a)


def description(num, txt):
    # msg = int(input(('choice a number, that show you the description of the comands: ')))
    # if msg == num:
    sleep(1)
    print(f'{list_comands[num]} - {txt} ')
    line()


def tips(msg, example):
    line()
    sleep(1)
    print(msg)
    print(f'example: {example}')
    line()


list_comands = ['MKDIR', 'RMDIR', 'CP',
                'MV', 'RM', 'CD', 'TOUCH', 'FIND A FILE']


linha('Here will be your guide for help you with comands in Linux')
print(f'\nChoice the type of comands. \n[1]- FILES \n[2]- TIPS')
choice = int(input('Which is the type: '))
if choice == 1:
    description(0, 'Purpose: to create a directory.')
    description(1, 'Purpose: to remove a directory.')
    description(2, 'Purpose: to make a copy of a file.')
    description(3, 'Purpose: to move a file to another location or rename it.')
    description(4, 'Purpose: to delete a file.')
    description(
        5, 'offers several ways to navigate and change the working directory using the terminal window')
    description(6, 'Purpose: create an empty file.')
    description(
        7, '(find) This is a powerful command for finding files in the file system.')

if choice == 2:
    tips('If you want to come back when to use the comand CD, only use two points ".."',
         '"name@name:~/Documents$ cd..')
