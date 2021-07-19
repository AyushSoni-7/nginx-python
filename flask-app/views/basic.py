from flask import Blueprint

basic_bp = Blueprint('basic_view', __name__)


@basic_bp.route("/", methods=["GET"])
def base():
    return "This is the base page", 200


@basic_bp.route("/blue", methods=["GET"])
def blue():
    return "Welcome to the blue app", 200


@basic_bp.route("/green", methods=["GET"])
def green():
    return "Welcom to the green app", 200

