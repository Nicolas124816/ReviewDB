from flask import Flask
from flask_cors import CORS

from board import pages

def create_app():
    app = Flask(__name__)
    CORS(app, origins="http://localhost:4200", supports_credentials=True)

    app.register_blueprint(pages.bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)