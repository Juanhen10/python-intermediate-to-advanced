# argparse.ArgumentParser para argumentos mais complexo
from argparse import ArgumentParser
from os import system

system('cls')


parser = ArgumentParser()


parser.add_argument(
    '-b', '--basic',
    help='Mostra "olá mundo" na tela ',
    type=str,
    metavar='STRING',
    default='ola mundo'
)

args = parser.parse_args()


if args.basic is None:
    print('Você não passou o valor de b')
else:
    print("você passou o valor")
