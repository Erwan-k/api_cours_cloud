from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from routes.personnes import personnes

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(personnes,"/personnes") 

if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')
