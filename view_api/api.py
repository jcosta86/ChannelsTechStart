from flask import Flask
from flask_restful import Api

from resources.channels_resource import ChannelsResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ChannelsResource, '/api/channels', endpoint='channels')
api.add_resource(ChannelsResource, '/api/channels/<int:id>', endpoint='channel')


@app.route('/')
def index():
    return 'Welcome to Channels!'


app.run(debug=True)
