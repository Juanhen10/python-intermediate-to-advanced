# secrets gera números aleatórios seguros
import os
import secrets
import string as s
from secrets import SystemRandom as sr

os.system('cls')

print(''.join(sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))


random = secrets.SystemRandom()

# print(secrets.randbelow(100))
# print(secrets.choice([10, 11, 12]))

# random.seed(0)


# r_range = random.randrange(10, 20, 2)
# print(r_range)

# r_int = random.randint(10, 20)
# print(r_int)

# r_uniform = random.uniform(10, 20)
# print(r_uniform)

# nomes = ['Juan', 'MAria', 'Helena', 'Joana']
# random.shuffle(nomes)

# novos_nomes = random.sample(nomes, k=2)
# print(novos_nomes)


# novos_nomes = random.choices(nomes, k=3)
# print(novos_nomes)
