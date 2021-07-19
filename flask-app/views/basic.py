from flask import Blueprint, jsonify, request


basic_bp = Blueprint('basic_view', __name__)


def headers(metadata):
    data = {
        "message": "This is the base page",
        "host": metadata.get("Host", "NULL"),
        "forward_for": metadata.get("X-Forwarded-For", "NULL"),
        "forwarded_proto": metadata.get("X-Forwarded-Proto", "NULL"),
        "upstream_addr": metadata.get("X-Upstream", "NULL")
    }
    return data


@basic_bp.route("/", methods=["GET"])
def base():
    data = request.environ
    retVal = headers(data)
    return jsonify(retVal), 200


@basic_bp.route("/blue", methods=["GET"])
def blue():
    retVal = metadata(request)
    retVal["message"] = "This is the blue page"
    return jsonify(retVal), 200

@basic_bp.route("/green", methods=["GET"])
def green():
    retVal = metadata(request)
    retVal["message"] = "This is the green page"
    return jsonify(retVal), 200
