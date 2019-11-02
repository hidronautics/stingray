from os import environ
from flask import jsonify


def create_response(status: bool, *args, **kwargs):
    if status:
        status = "success"
    else:
        status = "failure"

    response = {
        "status": status,
        "items": [args, kwargs]
    }
    return jsonify(response)


def get_env(name: str, default):
    if name in environ:
        return environ[name]

    return default
