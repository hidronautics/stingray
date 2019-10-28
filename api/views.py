from flask.views import MethodView
from flask import request
from auth_middleware import mw


class MyView(MethodView):
    decorators = [mw]

    def get(self):
        return "HI"

    def post(self):
        return "BYE"


class LaunchTest(MethodView):
    decorators = [mw]

    def get(self):
        return request.args

    def post(self):
        return "BYE"
