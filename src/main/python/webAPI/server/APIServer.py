"""
# encode: utf-8

"""

import flask
from flask import jsonify

from src.main.python.webAPI.server.Database import Database

app = flask.Flask(__name__)
app.config.update(
    DEBUG=True,
    TESTING=True,
    SECRET_KEY=b'DfKaH-kStZdHb0I7A13hAQ'
)
db = Database()


@app.route('/login', methods=['GET'])
def loginHTML():
    """Formulário HTML para logar"""
    return """
    <form action="/login" method="post">
  <div class="container">
    <label for="username"><b>Usuario</b></label>
    <input type="text" placeholder="Enter Username" name="username" required>
    <label for="password"><b>Senha</b></label>
    <input type="password" placeholder="Enter Password" name="password" required>
    <button type="submit">Login</button>
  </div>
</form>
    """


@app.route('/login', methods=['POST'])
def loginAPI():
    """Recebe usuario e senha via POST"""
    checkLogin = db.login(flask.request.form['username'], flask.request.form['password'])
    if checkLogin:
        flask.session['logged_in'] = True
        flask.session['user_id'] = checkLogin
        try:
            return getClientBooks(checkLogin)
        except Exception as e:
            print(e.__class__)
            print(e.__str__())
            return "Ocorreu um erro interno", 500
    else:
        flask.session['logged_in'] = False
        return "não foi possivel logar, verifique usuario ou senha!", 401


@app.route('/client/<id_client>/books', methods=['GET'])
def getClientBooks(id_client: int):
    """Listagem de livros emprestados"""
    if flask.session['logged_in']:
        try:
            resp = flask.Response(db.getBooksUser(id_client))
            resp.headers['Content-Type'] = 'application/json'
            resp.headers['Accept'] = 'application/json'
            resp.headers['charset'] = 'UTF-8'
            return resp
        except Exception as e:
            print(e.__class__)
            print(e.__str__())
            return "Ocorreu um erro interno", 500
    else:
        return "utilize o enpoint \login para autenticar", 401


@app.route('/books/<id_book>/reserve', methods=['POST', 'GET'])
def reserveBook(id_book: str):
    """Reserva de Livro para um usuario"""
    if flask.session['logged_in']:
        try:
            id_user = flask.session['user_id']
            resp = flask.Response(db.setBookToUser(id_book.__str__(), id_user.__str__()))
            resp.headers['Content-Type'] = 'application/json'
            resp.headers['Accept'] = 'application/json'
            resp.headers['charset'] = 'UTF-8'
            return resp
        except Exception as e:
            print(e.__class__)
            print(e.__str__())
            return "Ocorreu um erro interno", 500
    else:
        return "utilize o enpoint \login para autenticar", 401


@app.route('/books', methods=['GET'])
def getBooks():
    """Listagem de livros"""
    if flask.session['logged_in']:
        try:
            resp = flask.Response(db.getBooks())
            resp.headers['Content-Type'] = 'application/json'
            resp.headers['Accept'] = 'application/json'
            resp.headers['charset'] = 'UTF-8'
            return resp
        except Exception as e:
            print(e.__class__)
            print(e.__str__())
            return "Ocorreu um erro interno", 500
    else:
        return "utilize o enpoint \login para autenticar", 401


@app.route("/")
def site_map():
    """Lista de endpoints disponiveis"""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)


app.run()
