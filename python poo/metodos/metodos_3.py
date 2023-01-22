import os
os.system('cls')
# metodos vs @classmethod vs @staticmethod
# method -self, metodo de intancia
# @classmethod - cls, metodo de classe
# @staticmethod - metodo estáticos (Xself, Xcls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
        
    def set_user(self, user):
        # setter
        self.user = user
        
        
    def set_password(self, password):
        self.password = password
        
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
        
        
    @staticmethod
    def log(msg):
        print('LOG:', msg)
        
    
    
    
    
# c1 = Connection()
# c1.set_user('juan')
# c1.set_password(123)
c1 = Connection.create_with_auth('luiz', 123)
print(Connection.log('Teste'))
print(c1.user)
print(c1.password)
        