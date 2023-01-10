# System questions and answers
import os
from time import sleep
os.system('cls')
questions = {
    'question': 'how many is 2+2?',
    'option':['1','3','4','5'],
    'answers': '4'
}
questions2 = {
    'question': 'how many is 4*4?',
    'option':['16','4','3','18'],
    'answers': '16'
}
questions3 = {
    'question': 'how many is 9-8?',
    'option':['1','8','16','15'],
    'answers': '1'
}
tentativa = 0
p = 'S'
print('Hello!! Welcome the SUPEEEER questions x answers')
sleep(1)
while p in 'S':
    print(f'the first question.')
    print(f'{questions["question"]}')
    print('the options is...')
    sleep(0.2)
    for p in questions['option']:
        sleep(0.5)
        print(p)
    q = input('What is the correct option: ')
    if q == questions['answers']:
        int(questions['answers'])
        sleep(0.5)
        print(f'SUPEEEEER correct!!!!')
        p = str(input('do you want to continue?[S/N]:')).upper().strip()[0]
        if p == 'S':
            sleep(0.7)
            print('preparing for next question...')
        if p == 'N':
            break
    while q not in questions['answers']:
        t = input('try again: ')
        if t == questions['answers']:
            sleep(0.5)
            print(f'Finally you correct the question! SUPEEEER!')
            break
    p = str(input('do you want to continue?[S/N]:')).upper().strip()[0]
    if p == 'S':
        sleep(1)
        print(f'second question')
        print(f'{questions2["question"]}')
        sleep(1)
        print('the options is...')
        for p in questions2['option']:
            sleep(0.5)
            print(p)
        q = input('What is the correct option: ')
        sleep(0.5)
        if q == questions2['answers']:
            int(questions2['answers'])
            print('WOW! SSUPEEEEEER INTELIGENT. CORRECT QUESTION')
            p = str(input('do you want to continue?[S/N]:')).upper().strip()[0]
            if p == 'S':
                print('preparing for next question...')
            if p == 'N':
                break
        while q not in questions2['answers']:
            t = input('try again: ')
            if t == questions2['answers']:
                sleep(0.5)
                print(f'Finally you correct the question! SUPEEEER!')
                break
        p = str(input('do you want to continue?[S/N]:')).upper().strip()[0]     
        if p == 'S':
            sleep(1)
            print(f'second question')
            print(f'{questions3["question"]}')
            sleep(1)
            print('the options is...')
            for p in questions3['option']:
                sleep(0.5)
                print(p)
            q = input('What is the correct option: ')
            sleep(0.5)
            if q == questions3['answers']:
                int(questions3['answers'])
                print('SSUPEEEEEER. CORRECT QUESTION')
                p = str(input('do you want to continue?[S/N]:')).upper().strip()[0]
                if p == 'S':
                    print('preparing for next question...')
                if p == 'N':
                    break
            while q not in questions2['answers']:
                t = input('try again: ')
                if t == questions3['answers']:
                    sleep(0.5)
                    print(f'Finally you correct the question! SUPEEEER!')
                    break
            p = str(input('do you want to continue?[S/N]:')).upper().strip()[0]     

# ''''
# Resposta do professor!
# '''
# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]
# tentativa = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()
    
    
#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)
#     print()
#     escolha = input('escolha uma opção: ')
    
#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)
    
#     if escolha.isdigit():
#         escolha_int = int(escolha)
    
#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcao[escolha_int] == pergunta['Resposta']:
#                 acertou = True
#     print()        
#     if acertou:
#         tentativa += 1
#         print('acertou')
#     else:
#         print('errou')
        
#     print(f'Você acertou {tentativa} de {len(perguntas)} perguntas')