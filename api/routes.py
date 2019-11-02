from views import MainPage, Launch, Node, Sys, Topic

route_list = \
    [("/",                  MainPage.as_view("main_page"),    ["GET"]),
     ("/launch/",           Launch.as_view("launch_list"),    ["GET"]),
     ("/launch/<method>",   Launch.as_view("launch_control"), ["POST"]),
     ("/nodes",             Node.as_view("nodes"),            ["GET"]),
     ("/topics",            Topic.as_view("topics"),          ["GET"]),
     ("/sys",               Sys.as_view("system"),            ["GET", "POST"]),
     ]
