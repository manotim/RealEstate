from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS

import os

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    
    # Explicitly allow CORS for the frontend
    CORS(app, supports_credentials=True)

    # Register blueprints
    from app.auth import auth_bp
    from app.routes import main_bp, mpesa_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp, url_prefix="/api")
    app.register_blueprint(mpesa_bp, url_prefix="/mpesa")

    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to Edu House!"})

    @app.route("/test")
    def test():
        return jsonify({"message": "Test route is working!"})

    # Add CORS headers after each request
    @app.after_request
    def add_cors_headers(response):
        print("Adding CORS headers")  # Debugging line
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:5173"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response

    return app
