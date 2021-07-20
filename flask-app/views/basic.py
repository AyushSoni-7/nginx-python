from flask import Blueprint, jsonify, request
import socket

basic_bp = Blueprint('basic_view', __name__)


def headers(metadata):
    host_name = socket.gethostname()
    data = {
        "message": "This is the base page",
        "host": metadata.get("Host", "NULL"),
        "client_ip": metadata.get("X-Forwarded-For", "NULL"),
        "forwarded_proto": metadata.get("X-Forwarded-Proto", "NULL"),
        "host_name": host_name,
        "server_ip": socket.gethostbyname(host_name)
    }
    return data


@basic_bp.route("/", methods=["GET"])
def base():
    data = request.headers
    retVal = headers(data)
    return retVal, 200


@basic_bp.route("/blue", methods=["GET"])
def blue():
    data = request.environ
    retVal = headers(data)
    retVal["message"] = "This is the blue page"
    return jsonify(retVal), 200


@basic_bp.route("/green", methods=["GET"])
def green():
    data = request.environ
    retVal = headers(data)
    retVal["message"] = "This is the green page"
    return jsonify(retVal), 200

