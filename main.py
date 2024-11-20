from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/template/registropersonal')
def registropersonal():
    return render_template('registropersonal.html')


@app.route('/template/solicitudyquejas')
def solicitudyquejas():
    return render_template('solicitudyquejas.html')


@app.route('/template/gestionpago')
def gestionpago():
    return render_template('gestionpago.html')


@app.route('/template/gestionresidente')
def gestionresidente():
    return render_template('gestionresidente.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
