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


def description(lista, num, txt):
    # msg = int(input(('choice a number, that show you the description of the comands: ')))
    # if msg == num:
    sleep(1)
    print(f'{lista[num]} - {txt} ')
    line()


def tips(msg, example=None):
    sleep(1)
    print(msg)
    if example is not None:
        print(f'what doing: {example}')
    line()


list_file = ['MKDIR', 'RMDIR', 'CP',
             'MV', 'RM', 'CD', 'TOUCH', 'FIND A FILE']

list_ls = ['ls', 'ls -l', 'ls -a', 'ls -h', 'ls -ltr']

list_cat = ['cat', 'cat -n', 'cat > [name]']


linha('Here will be your guide for help you with comands in Linux')
print(
    f'\nChoice the type of comands. \n[1]- FILES \n[2]- TIPS \n[3]- CTRL + [comand3] \n[4]- LS \n[5]- CAT ')
choice = int(input('Which is the type: '))
line()
if choice == 1:
    description(list_file, 0, 'Purpose: to create a directory.')
    description(list_file, 1, 'Purpose: to remove a directory.')
    description(list_file, 2, 'Purpose: to make a copy of a file.')
    description(
        list_file, 3, 'Purpose: to move a file to another location or rename it.')
    description(list_file, 4, 'Purpose: to delete a file.')
    description(list_file,
                5, 'offers several ways to navigate and change the working directory using the terminal window')
    description(list_file, 6, 'Purpose: create an empty file.')
    description(list_file,
                7, '(find) This is a powerful command for finding files in the file system.')

if choice == 2:
    tips('If you want to come back when to use the comand CD, only use two points ".." or "~" is going to home of the user')
if choice == 3:
    tips('CTRL + T', 'Open the terminal')
    tips('CTRL + L', 'Clean the terminal')
    tips('CTRL + C', 'Break the program')

if choice == 4:
    description(list_ls,
                0, 'is the comand that make a list of all file in your Linux')
    description(list_ls, 1, 'show sthe file with details')
    description(list_ls, 2, 'shows the ocults file')
    description(list_ls, 3, 'shows the two comands (ls -l and ls-a) ')
    description(
        list_ls, 4, 'shows the list in detail but though the date')
if choice == 5:
    description(list_cat, 0, 'show the files')
    description(
        list_cat, 1, 'shows the line detail you can choose to change the file')
    description(list_cat, 2, 'Create a new file')


# comando history mostra o historico de comandos usados
# ctrl + r mostrará uma barra de pesquisa, para procurar comandos
