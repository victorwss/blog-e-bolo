from flask import Flask, redirect, render_template, request
from werkzeug.wrappers.response import Response

from model.blog_model import Materia, MateriaSemId, MateriaVazia, MateriaNaoEncontrada
from model.blog_dao_mem import BancoDeDadosMateria

app = Flask(__name__)

db = BancoDeDadosMateria()

# COLOQUE O SEU CÓDIGO AQUI. POR EXEMPLO:
#
# @app.route("/algum_lugar/<algum_parametro>", methods = ["POST"])
# def alguma_coisa(algum_parametro: str) -> Respose | str:
#     x = AlgumaCoisa(**request.form).algum_metodo(algum_parametro)
#     resultado = db.algum_outro_metodo(x)
#     return render_template("algum_template.html", algum_valor = resultado)

if __name__ == "__main__":
    app.run("0.0.0.0", port = 5001, debug = True)