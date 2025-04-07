from app import app, login, library, admin
from app.db import create_db
from os import path

if __name__ == '__main__':
    """
    Pokud se jedná o hlavní soubor, tak se inicializuje databáze
    """
    if not path.exists(app.config["DATABASE"]):
        create_db()
        print("inicializace database")

    app.register_blueprint(login.bp)
    app.register_blueprint(library.bp)

    app.register_blueprint(admin.bp)
    """
    Pokud se jedná o hlavní soubor, tak se spustí aplikace
    """
    app.run(debug=True)


