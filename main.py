import eventlet
import json
import time

from flask import Flask
from threading import Thread
from flask_mqtt import Mqtt
from flask_socketio import SocketIO

from users import users
from weather import weather
from status import get_status
from music import music
from light import light
from auth import bp

eventlet.monkey_patch()


app = None
mqtt = None
socketio = None
thread = None


def create_app():
    global app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'PDS19UkUAd1H1NiAqJjGAFT6KrN78W5J'

    app.register_blueprint(bp)
    app.register_blueprint(users)
    app.register_blueprint(light)
    app.register_blueprint(music)
    app.register_blueprint(weather)

    @app.route('/')
    def welcome():
        global thread
        if thread is None:
            thread = Thread(target=background_thread)
            thread.daemon = True
            thread.start()
        return 'Welcome to Hue!'

    return app


def create_mqtt_app():
    # Setup connection to mqtt broker
    app.config['MQTT_BROKER_URL'] = '127.0.0.1'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_KEEPALIVE'] = 5
    app.config['MQTT_TLS_ENABLED'] = False

    global mqtt
    mqtt = Mqtt(app)
    global socketio 
    socketio = SocketIO(app, async_mode="eventlet")

    return mqtt

# Start MQTT publishing
# Function that every second publishes a message
def background_thread():
    count = 0
    while True:
        time.sleep(1)
        # Using app context is required because the get_status() functions
        # requires access to the db.
        with app.app_context():
            message = json.dumps(get_status(), default=str)
        # Publish
        mqtt.publish('python/mqtt', message)

# App will now have to be run with `python app.py` as flask is now wrapped in socketio.
# The following makes sure that socketio is also used

def run_socketio_app():
    create_app()
    create_mqtt_app()
    socketio.run(app, host='127.0.0.1', port=5000, use_reloader=False, debug=True)

if __name__ == '__main__':
    run_socketio_app()