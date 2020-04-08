# Flask-RESTful video-jonesdebu
video-jonesdebu created by GitHub Classroom
## Be sure to run:
* sudo apt-get install libsm6 libxrender1 libfontconfig1
* It is required for opencv-python to work. Opencv python is used to create the video.

## How to run
* import a kyes file to access the twitter api
* python application.py
* open browser and go to localhost:5000 to create the api
* go to localhost:5000/createvideo to create the video with the media from a test twitter user account
* go to locathost:5000/downloadvideo to download the video that was created from the previous webpage

##Description
* This application will create and download a video summary of the tweets and media from my test twitter account. Devs can change the user by going into applicaiton.py and changing 'Donovan01060515' to a different user in images = user_images(api, 'Donovan01060515') at line 19.

## Problems
* unable to get the flask application working on AWS.
* When running the web server returns a {server address} refused to connect error_statement
