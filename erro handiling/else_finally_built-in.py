import os
os.system('cls')


try:
    print('abri')
    8/1
except ZeroDivisionError:
    print('DIVIDIU ZERO')
else:
    print('sem erro')
finally:
    print('fechar Arquivo')