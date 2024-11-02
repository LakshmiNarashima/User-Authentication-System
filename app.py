from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from auth import auth_bp
from models import db

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy with app
db.init_app(app)

# Register authentication blueprint
app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the User Authentication System!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
