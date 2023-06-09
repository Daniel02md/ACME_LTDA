from flask import Flask, request, jsonify
from flask_cors import cross_origin
from controllers.Funcionario import FuncionarioController
from config import app_config, app_activate


config = app_config[app_activate]

def create_app(*config_name) -> Flask: 
    app = Flask(__name__)
    app.config.from_object(config)


    @app.route('/funcionario', methods=["POST"])
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def insert_funcionario():
        response = FuncionarioController().insert(
            **request.form.to_dict()
        )
        
        return jsonify(response.response), response.code



    @app.route('/funcionario', methods=["GET"])
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get_funcionario_by_alpha():
        results = FuncionarioController().get_alpha_order()
        return jsonify(results.response), results.code



    @app.route('/funcionario/<int:id>', methods=["GET"])
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get_funcionario_by_ID(id: int):
        funcionario = FuncionarioController().get_by_ID(id=id)
        if funcionario:
            return jsonify(funcionario.response), funcionario.code
        else:
            return jsonify(funcionario.response), funcionario.code

    
    @app.route('/funcionario/<int:id>', methods=["POST"])
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def update_funcionario(id=None):
        response = FuncionarioController().update(id=id, **request.form.to_dict())
        return jsonify(response.response), response.code 
    

    @app.route('/funcionario/<int:id>', methods=["DELETE"])
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def delete_funcionario(id=None):
        response = FuncionarioController().delete(id=id)
        return jsonify(response.response), response.code
    
    return app
