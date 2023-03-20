# Deque - Trabalhando com LIFO e FIFO
# deque - Double-ended queue
# Lifo(pilha) e fifo(fila)


# LIFO  (Last In First Out)
# Pilha (stack)
# Significa que o último item a entrar será o priemiro a sair (list)
# Artigo:
# https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-lista-stack/
# Video:
# https://youtu.be/svWVHEihyNI
# Para tirar itens do final:  0(1) Tempo constante
# Para tirar itens do início: 0(n) Tempo Linear

from collections import deque

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ✅Legal (LIFO com lista)
# 0 1 2 3 4 5 6 7 8 9
# [0 1 2 3 4 5 6 7 8 9]
lista.append(10)
# 0 1 2 3 4 5 6 7 8 9 10
# [0 1 2 3 4 5 6 7 8 9 10]
lista.append(11)
# 0 1 2 3 4 5 6 7 8 9 10 11
# [0 1 2 3 4 5 6 7 8 9 10 11]
ultimo_removido = lista.pop()
# 0 1 2 3 4 5 6 7 8 9 10
# [0 1 2 3 4 5 6 7 8 9 10]
print('Último:', ultimo_removido)
print('Lista:', lista)
# 0 1 2 3 4 5 6 7 8 9 10
# [0 1 2 3 4 5 6 7 8 9 10]
print()


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 🚫Ruim (FIFO com lista)
# 0 1 2 3 4 5 6 7 8 9
# [0 1 2 3 4 5 6 7 8 9]
lista.insert(0, 10)
# 0 1 2 3 4 5 6 7 8 9 10
# [10 0 1 2 3 4 5 6 7 8 9]
lista.insert(0, 11)
# 0 1 2 3 4 5 6 7 8 9 10 11
# [0 1 2 3 4 5 6 7 8 9 10 11]
primeiro_removido = lista.pop(0)
# 0 1 2 3 4 5 6 7 8 9 10 11
# [11 0 1 2 3 4 5 6 7 8 9 10]
print('Último:', primeiro_removido)
print('Lista:', lista)
# 0 1 2 3 4 5 6 7 8 9 10
# [0 1 2 3 4 5 6 7 8 9 10]
print()

# FIFO (first In First Out)
# Filas (queue)
# Significa que o primeiro item a entrar será o primeiro a sair (deque)
# Artigo:
# https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
# Vídeo:
# https://youtu.ne/Rhb-8hXs3HE
# PAra tirar itens do final: 0(1) tempo constante
# Para tirar itens do início: 0(1) Tempo constante

# ✅Legal (Fifo com deque)

filas_correta: deque[int] = deque()
filas_correta.append(3)
filas_correta.append(4)
filas_correta.append(5)
filas_correta.appendleft(0)
filas_correta.appendleft(1)
filas_correta.appendleft(2)
print(filas_correta)
filas_correta.pop()
filas_correta.popleft()
print(filas_correta)
