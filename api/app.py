from flask import Flask
from routes import *

app = Flask(__name__)

if __name__ == '__main__':
    for path, view_func, methods in route_list:
        app.add_url_rule(rule=path, view_func=view_func, methods=methods)
    app.run(debug=False, port=8080, host="0.0.0.0", use_reloader=False, threaded=False)
