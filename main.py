from app import app, login

app.register_blueprint(login.bp)

if __name__ == '__main__':
    app.run(debug=True)
