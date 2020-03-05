from flask import Flask
from flask_restful import Resource, Api
from twitter_api import create_api, user_images, vid_creator

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        api = create_api("keys")
        images = user_images(api, 'Donovan01060515')
        return {'items found in user Donovan01060515 twitter feed' : str(len(images))}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
