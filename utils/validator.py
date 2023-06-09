class CPF:
    def __init__(self, cpf):
        self.cpf = cpf

    
    def validate(self):
        cpf = self.digit

        if len(cpf) != 11 or not cpf.isdigit():
            return False
        
        if len(set(cpf)) == 1:
            return False
        
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        primeiro_dig = (soma * 10) % 11
        if primeiro_dig == 10:
            primeiro_dig = 0
        if primeiro_dig != int(cpf[9]):
            return False

        
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        segundo_dig = (soma * 10) % 11
        if segundo_dig == 10:
            segundo_dig = 0
        if segundo_dig != int(cpf[10]):
            return False

        return True

    @property
    def digit(self):
        cpf = self.cpf.replace(".", "").replace("-", "")
        return cpf