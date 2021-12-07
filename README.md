# PyPrototype-DashDesk-Plugin

This app is used to demonstrate the plug in architecture using dash framework in python.

## What it does?

Basically, there is a home application (home_index.py - A dash application - which has it's own server & UI) which has the capability to load one plugin at a time. It will list down all the plugins in the "plugins" folder as a buttons. When user clicks the button, the home application, starts the selected plug in application in a different server & routes to that server

Plug in application is also another application which can run separately. 

There is no actual link between home & plug in. Whenever user want to go to certain plug in, home application, starts the plug in application & routes to that server.

To create web application **Dash** is used.
To host url in the desktop window **pywebview** is used.
**Pipenv** is used to track dependencies