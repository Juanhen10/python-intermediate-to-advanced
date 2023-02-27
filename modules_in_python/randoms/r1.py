import os
import random
import time

os.system("cls")
# random tem geradores de números pseudoaleatorios
# Obs.: números pseudialeatórios significa que os números parecem ser aleatórios, mas na verdade
# não são
# Portanto, este módulo não deve ser usado par asegurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo, a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html

# Funções:
# seed
#  -> Inicializa o gerador de random(por isso "números pseudoaleatorios")
random.seed(0)


# random.randrange(inicio, fim, passo)
r_range = random.randrange(10, 20, 2)
print(r_range)
#  -> Gera um número inteiro aleatório dentro de um intervalo especifico
# random.randint(inicio, fim)
r_int = random.randint(10, 20)
print(r_int)
#  -> Gera um número inteiro aleatorio dentro de um intervalo sem passo"
# random.uniform(inicio, fim)
r_uniform = random.uniform(10, 20)
print(r_uniform)
#  -> gera um número flutuante dentro de um intervalo "sem"
# random.shuffle(SequenciaMutável) -> Embralha a lista original
# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Juan', 'MAria', 'Helena', 'Joana']
random.shuffle(nomes)
# print(nomes)
# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=2)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(novos_nomes)


# random.choice(Iterável) -> Escolhe
print(random.choice(nomes))
