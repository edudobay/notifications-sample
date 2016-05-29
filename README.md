# Sample project

This is a toy web project that I am using to study some front-end web technology that I'm not yet very familiar with; this includes WebSockets, HTML5 APIs (such as the Notifications API), ECMAScript 2015, JS modules, SASS, some JS tools like WebPack, etc.

Well, it is called `notifications-sample` for the time being because I have started with a simple interface for showing notifications that come in a websocket :laughing:

## Instructions

### Front-end

* `npm install`
* All scripts I need to build the static files are in the `scripts` section in `package.json` (so you can just `npm run` them). It also helps to install these globally (`npm install -g WHATEVER`):
  - `webpack`
  - `gulp`
  - optionally, `browser-sync` (it is not listed as a dependency)

### Python

I used Python for writing a simple WebSockets backend.  Python sources are in the `python-server` folder.

* **Python ≥ 3.4.4** is needed (3.4 because of *asyncio* and 3.4.4 because of *asyncio.ensure_future*)
* `pip install -r requirements.txt` to install further dependencies
* To run it, just execute the `python-server/notification_server.py` file

