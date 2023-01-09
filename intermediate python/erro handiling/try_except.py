import os
os.system('cls')
# try, except, else e finally
try:
    a = 18 
    b = 0
    c = a / b
except ZeroDivisionError as error:
    print('Impossivel dividr por zero')
    print(error)
    print(error.__class__.__name__)
except NameError:
    print('Nome não definido')
except (TypeError, IndexError):
    print('erro de tipo ')
except Exception:
    print('erro desconhecido')
    
    