from models.Funcionario import Funcionario
from utils.validator import CPF
from utils.response_handler import Response


class FuncionarioController:
    def __init__(self) -> None:
        self.model_funcionario = Funcionario()

    def insert(self, cpf: str, nome: str, cargo: str, salario: float) -> dict:

        cpf = CPF(cpf=cpf)

        if not cpf.validate():
            return  Response().error.invalid_values("cpf")

        if self.model_funcionario.already_cpf_exists(cpf=cpf.digit):
            return  Response().error.conflict("cpf")
    
        if not nome:
            return Response().error.null_value("nome")
        if not cargo:
            return Response().error.null_value("cargo")
        if not salario:
            return Response().error.null_value("salario")
        else:
            try:
                float(salario)
            except:
                return Response().error.invalid_values("salario")

        self.model_funcionario.insert(
            cpf=cpf.digit,
            nome=nome,
            cargo=cargo,
            salario=float(salario)
        )
        
        return Response().success.created()

        
        
            
    def get_alpha_order(self) -> dict:
        results = []
        for result in self.model_funcionario.get_alpha_order():
            results.append(
                {
                    "ID": result.Funcionario.ID,
                    "CPF": result.Funcionario.CPF,
                    "nome": result.Funcionario.NOME,
                    "cargo": result.Funcionario.CARGO,
                    "salario": result.Funcionario.SALARIO
                }
            )
        return Response().success.results(results)
            



    def get_by_ID(self, id) -> dict:
        funcionario = self.model_funcionario.get_by_ID(id=id)
        if funcionario:
            result = {
                    "ID": funcionario.Funcionario.ID,
                    "CPF": funcionario.Funcionario.CPF,
                    "nome": funcionario.Funcionario.NOME,
                    "cargo": funcionario.Funcionario.CARGO,
                    "salario": funcionario.Funcionario.SALARIO
                }
            return Response().success.results(result)
        else:
            return Response().error.does_not_exist("ID")
        
        
    def update(self, id=None, cpf=None, nome=None, cargo=None, salario=None):
        if not id:
            return Response().error.null_value("ID")
        
        if not self.model_funcionario.get_by_ID(id=id):
            return Response().error.does_not_exist("ID")
        
        if cpf:
            cpf = CPF(cpf).digit

            if not CPF(cpf).validate():
                return Response().error.invalid_values("cpf")
            
            if self.model_funcionario.already_cpf_exists(cpf):
                cpf = None

        if salario:
            try:
                float(salario)
            except:
                return Response().error.invalid_values("salario")
            
        response = {}
        for key, value in dict(cpf=cpf, nome=nome, cargo=cargo, salario=salario).items():
            if value:
                response[key.upper()] = value

        self.model_funcionario.update(id=id, **response)
        return Response().success.updated()


    def delete(self, id=None) -> Response:
        if not id:
            return Response().error.null_value("ID")
        
        if self.model_funcionario.get_by_ID(id=id):
            if self.model_funcionario.delete(id=id):
                return Response().success.deleted()
        else:
            return Response().error.does_not_exist("ID")