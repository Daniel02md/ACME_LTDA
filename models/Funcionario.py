from sqlalchemy.types import INTEGER, VARCHAR, DOUBLE
from sqlalchemy import Column, Identity
from sqlalchemy.sql.expression import select, insert, update, delete
from . import db, app

# RETURN REFERENCE IMPORTS
from typing import Sequence, Optional
from sqlalchemy.engine.row import Row
from sqlalchemy.engine.result import _TP
# =============================

class Funcionario(db.Model):
    
    ID = Column(INTEGER,  Identity(start=1, increment=1), primary_key=True, nullable=False)
    CPF = Column(VARCHAR(11), unique=True, nullable=False)
    NOME = Column(VARCHAR(255), nullable=False)
    CARGO = Column(VARCHAR(100), nullable=False)
    SALARIO = Column(DOUBLE, nullable=False)


    def insert(self, cpf: str, nome: str, cargo: str, salario: float) -> bool:
        try:
            with app.app_context():
                db.session.execute(
                    insert(Funcionario).values(
                        CPF=cpf,
                        NOME=nome,
                        CARGO=cargo,
                        SALARIO=salario
                    )
                )
                
                db.session.commit()
                
        except Exception as e:
            print(e)
            return False
        
            

    def get_alpha_order(self) -> Sequence[Row[_TP]]:
        try:
            with app.app_context():
                print(db.session.execute(select(Funcionario).order_by(Funcionario.NOME)).all())
                results = db.session.execute(select(Funcionario).order_by(Funcionario.NOME)).all()
        except: 
            results = []
        finally:
            return results


    def get_by_ID(self, id) -> db.Model:
        try:
            with app.app_context():
                result = db.session.execute(select(Funcionario).where(Funcionario.ID == id)).first()
        except:
            result = []
        finally:
            return result
        
        
    def already_cpf_exists(self, cpf: str) -> bool:
        try: 
            with app.app_context():
                result = db.session.execute(select(Funcionario).where(Funcionario.CPF==cpf)).first()
        except:
            result = []
        finally:
            if result:
                return True
            else:
                return False
            


    def update (self, id, **kwargs) -> bool:
        try: 
            with app.app_context():
                db.session.execute(
                    update(Funcionario)
                    .where(Funcionario.ID == id)
                    .values(**kwargs)
                )
                db.session.commit()
            return True
        
        except Exception as e:
            print(e)
            return False

    def delete(self, id) -> bool:
        try:
            with app.app_context():
                db.session.execute(
                    delete(Funcionario).where(Funcionario.ID == id)
                )
                db.session.commit()
                return True
        except Exception as e:
            print(e)
            return False