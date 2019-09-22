from flask import Flask
from routes import *
from views import *

app = Flask(__name__)

if __name__ == '__main__':
    # app.add_url_rule(view_func=)
    for path, view_func in route_list:
        app.add_url_rule(path, view_func=view_func)
    app.run(debug=True, port=8080, host="192.168.0.96")
