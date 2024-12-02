# be/app.py
from flask import Flask
from controllers.controller import sao_ke_blueprint
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(sao_ke_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
