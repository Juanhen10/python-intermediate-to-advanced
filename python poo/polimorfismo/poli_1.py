import os 
os.system('cls')
# Polimorfismo em Python Orientado a Objetos
# Polimortfismo é o princípio que permite que classes derivadas de uma sua mesma superclasse
# tenham métodos iguais (com mesma assinatura) mas comportamento diferentes.
# Assisnatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetro e retorno iguais
# SO "L"ID
# Princípop da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação
# Sobrecarga de métodos (overlload) 🐍 = ❌
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        
    @abstractmethod
    def enviar(self) -> bool:
        ...
        
        
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False
        
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('Notificação enviada')
    else: 
        print('Notificação não enviada')
        
notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando sms')
notificar(notificacao_sms)