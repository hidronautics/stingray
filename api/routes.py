from views import MainPage, Launch, Node, Sys, Topic

route_list = \
    [("/",       MainPage.as_view("main_page")),
     ("/launch", Launch.as_view("launch")),
     ("/nodes",  Node  .as_view("nodes")),
     ("/sys",    Sys   .as_view("system")),
     ("/topics", Topic .as_view("topics")),
     ]
