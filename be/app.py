# be/app.py
from flask import Flask
from controllers.controller import sao_ke_blueprint

app = Flask(__name__)
app.register_blueprint(sao_ke_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
