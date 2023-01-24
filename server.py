from flask_app import app
# 1) import application

from flask_app.controllers import users
# 2) import routes

if __name__ == "__main__":
    app.run(debug=False, port=80)
# 3) if in file runexit