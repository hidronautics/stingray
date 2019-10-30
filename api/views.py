from flask.views import MethodView
from flask import request, abort
from auth_middleware import mw
from ros_launch_handlers import LaunchFile

launch = LaunchFile("")


class MainPage(MethodView):
    decorators = [mw]

    def get(self):  # TODO:remove that msg
        greeting_msg = """
        Welcome to ROS launch REST service
        we have cookies in here
        if u want to:
            start or stop launch file POST /launch?what=[start/stop]&param_name1=val1&param_name2=val2
            look at launch files GET /launch
            look at launch files GET /launch/start
            checkout video stream GET /...
            look at specific topic GET /topics?topic_name=params
            list nodes GET /nodes
            system info GET /sys
            shutdown/reboot POST /sys?cmd=[reboot/shutdown]
            /sys/reboot"""
        return greeting_msg


class Launch(MethodView):
    decorators = [mw]

    def get(self):
        kwargs = dict(request.args)
        file = kwargs.get("what")
        if file is None:
            abort(400)
        kwargs.pop("what")

        method = kwargs.get("method")
        kwargs.pop("method")
        # TODO: start launch files from POST
        global launch
        if method == "start":
            launch = LaunchFile(file, kwargs)
            launch.start()
        if method == "stop":
            launch.stop()

        return request.args

    def post(self):
        return "BYE"


class Topic(MethodView):
    decorators = [mw]

    def get(self):
        return request.args

    def post(self):
        return "BYE"


class Node(MethodView):
    decorators = [mw]

    def get(self):
        return request.args

    def post(self):
        return "BYE"


class Sys(MethodView):
    decorators = [mw]

    def get(self):
        return request.args

    def post(self):
        return "BYE"

