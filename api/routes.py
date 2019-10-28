from views import *

route_list = \
    [("/", MyView.as_view('mw')),
     ("/launch", LaunchTest.as_view('launch')), ]
