# importing libraries
from flask import Flask
from flask_restful import Api, Resource, reqparse

import csv 
import sys
import pprint

app = Flask(__name__)
api = Api(app)

# Reading the csv file into a dictionary
reader = csv.DictReader(open('ra_data_classifier.csv', 'rb'))
dict_list = []

for line in reader:
	dict_list.append(line)

# User resource class with GET and POST HTTP request methods
class User(Resource):

	def get(self, hid):
		for user in dict_list:
			if(hid == user["hid"]):
				return user, 200
		return "Hid not found", 404

	def post(self, hid):
		parser = reqparse.RequestParser()
		parser.add_argument("chunk")
		parser.add_argument("has space")
		args = parser.parse_args()

		for user in dict_list:
			if(hid == user["hid"]):
				return "Data with hid {} already exists".format(hid), 400

		user = {
			"hid": hid,
			"chunk":args["chunk"],
			"has space": args["has space"]
		}

		# Add the new user to the dictionary
		dict_list.append(user)

		# Write the data to the csv file
		myFile = open('ra_data_classifier.csv', 'w')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows(user)

		myFile.close()
		return user, 201

api.add_resource(User, "/user/<string:hid>")
app.run(debug = True)

