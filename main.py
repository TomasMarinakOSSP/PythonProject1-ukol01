from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        radio = request.form['radio']
        if username == 'pokuston' and password == 'heslo':
            flash('Přihlášení bylo úspěšné!', 'success')
        else:
            flash('Přihlášení selhalo! Zkuste to znovu.', 'warning')
        return render_template('index.html', username=username, password=password, radio=radio)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
