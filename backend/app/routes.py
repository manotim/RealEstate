from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)
mpesa_bp = Blueprint("mpesa", __name__)

@main_bp.route("/")
def home():
    return jsonify({"message": "Welcome to the Apartment Management System!"})



@mpesa_bp.route("/payment", methods=["GET"])
def process_payment():
    return {"message": "Mpesa payment endpoint"}