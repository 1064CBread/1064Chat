from flask import Blueprint, Flask, render_template, request

blueprint = Blueprint(__name__, __name__, url_prefix='/auth')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method != 'POST':
        return render_template("login_start.jinja")
    print(request.form)
    return 'You "logged" in. EMAIL: ' + request.form['email'] + '; PASS: ' + request.form['password']


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method != 'POST':
        return render_template("register_start.jinja")
    return 'You "register" an account. EMAIL: ' + request.form['email'] + '; PASS: ' + request.form['password']


def registerself(app: Flask, prefix=''):
    app.register_blueprint(blueprint, url_prefix=prefix + blueprint.url_prefix)
