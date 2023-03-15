from threading import Thread
from time import sleep

'''
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('OI!', 10))
t2.start()


for i in range(10):
    print(i)
    sleep(.5)
'''


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo!', 10))
t1.start()
t1.join()

print('Thread acabou!')


# while t1.is_alive():
#     print('Esperando a thread.')
#     sleep(2)
