from flask import Flask, send_file, send_from_directory
from flask_restful import Resource, Api
from twitter_api import create_api, user_images, vid_creator

application = Flask(__name__)
api = Api(application)

#arguments hardcoded until solution to passing arguments int the get function is found.

class get_create_api(Resource):
    def get(self, keys = "keys"):
        api = create_api("keys")
        #images = user_images(api, 'Donovan01060515')
        return {'api' : 'created'}

class CreateVideo(Resource):
    def get(self):
        api = create_api("keys")
        images = user_images(api, 'Donovan01060515')
        vid_creator(images, 'static', 'my_vid')
        #send_file('static/my_vid.avi')

class DownloadVideo(Resource):
    def get(self):
        #@app.route('/static')
        #send_from_directory('static', 'my_vid.avi', as_attachment=True)
        return send_file('static/my_vid.avi')
        #return {'video' : 'downloaded'}




api.add_resource(get_create_api, '/', '/<string:keys>')
api.add_resource(CreateVideo, '/createvideo')
api.add_resource(DownloadVideo, '/downloadvideo')



if __name__ == '__main__':
    application.run(debug=True, port=5000)
