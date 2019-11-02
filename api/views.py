from flask.views import MethodView
from flask import request, abort, jsonify
from auth_middleware import mw
from ros_handlers import LaunchFile, TopicsUtil
from utils import create_response
from roslaunch.parent import RLException

launch_dict = dict()


class MainPage(MethodView):
    decorators = [mw]
    methods = ["GET"]

    def get(self):  # TODO:remove that msg
        greeting_msg = jsonify({
            "msg": [
                "Welcome to ROS launch REST service",
                "we have cookies in here",
                "if u want to:",
                "look at launch files GET /launch",
                "start/stop launch file POST /launch/[start/stop]?what=filename",
                "checkout video stream GET /...",
                "list topics GET /topics",
                "look at specific topic GET /topics/<topic_name>",
                "list nodes GET /nodes",
                "system info GET /sys",
                "shutdown/reboot POST /sys/<[reboot/shutdown]>"]})
        return greeting_msg


class Launch(MethodView):
    decorators = [mw]
    methods = ["GET", "POST", "DELETE"]
    global launch_dict

    def get(self):
        return create_response(True, *launch_dict.keys())

    def post(self, method):
        kwargs = dict(request.args)
        filename = kwargs.get("what")
        if filename is None:
            abort(400)

        kwargs.pop("what")

        if method == "start":
            launch_dict[filename] = LaunchFile(filename, kwargs)
            try:
                launch_dict[filename].start()
            except RLException:
                launch_dict.pop(filename)
                abort(400)

            return create_response(True, filename, **kwargs)

        elif method == "stop":
            if  filename not in launch_dict.keys():
                abort(400)

            launch_dict[filename].stop()
            launch_dict.pop(filename)
            return create_response(True, filename)

        else:
            return create_response(False)


class Topic(MethodView):
    decorators = [mw]
    methods = ["GET"]

    def get(self):
        return create_response(True, TopicsUtil().get_all())


class Node(MethodView):
    decorators = [mw]
    methods = ["GET"]

    def get(self):
        return request.args


class Sys(MethodView):
    decorators = [mw]
    methods = ["GET", "POST"]

    def get(self):
        return request.args

    def post(self):
        return "BYE"
