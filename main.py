from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/abc')
def abc():
    return render_template('abc.html')


@app.route('/azb')
def azb():
    return render_template('azb.html')


@app.route('/alpha')
def alpha():
    return render_template('alfa.html')


@app.route('/heb')
def heb():
    return render_template('heb.html')


if __name__ == '__main__':
    app.run(debug=True)
