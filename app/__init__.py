from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    return render_template('index.html')