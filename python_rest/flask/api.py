from flask import Flask
from flask_restful import Resource, Api, reqparse

import csv
import sys

# from sqlalchemy import create_engine
# from json import dumps
# from flask.ext.jsonpify import jsonify

# db_connect = create_engine('sqlite:///ra_data_classifier.csv')
app = Flask(__name__)
api = Api(app)

# number = "33BFF6QPI1YEFYISIWWDVQKGH8RW3Z"
# number2 = "3HUR21WDDUCUK1K6HMLPN3U0ZBSYX0"
csv_file = csv.reader(open('ra_data_classifier.csv', "rb"), delimiter=",")

# hids = []
# match = ""

data = []
for row in csv_file:
	print row
# 	data = row
# 	row1 = next(csv_file)
# 	match = row1[0]
# 	break
# print match
# print number2
	# print match
# 	if(number2 == match)
# 		break
# print match
	# hids = row[0]
	# for row in hids:
	# 	print hids[0]
# for row in hids
# 	if number 
# for row in csv_file:
# 	if (number == row[0])
# 		print row


# with open('ra_data_classifier.csv', 'rb') as csvfile:
# 	reader = csv.reader(csvfile)
# 	hid = '33BFF6QPI1YEFYISIWWDVQKGH8RW3Z'
# 		# csv_file = csv.reader(open('ra_data_classifier.csv', "rb"), delimiter=",")
# 	for row in reader:
# 		print row[0]
		# match = row[0]
		# if hid == match
		# 	print row
		# if search == row[1]
		# results.append(row)

# datas = [
# 	{
# 		"hid": "33BFF6QPI1YEFYISIWWDVQKGH8RW3Z",
# 		"chunk": "Landmark Center, 8th Fl",
# 		"has space": 0
# 	},
# 	{
# 		"hid": "3HUR21WDDUCUK1K6HMLPN3U0ZBSYX0",
# 		"chunk": "Contact: The C3 team at MakemeC3@cic.us -- Additional information at www.cambridgecoworking.com.",
# 		"has space": 0
# 	}
# ]

class User(Resource):
	def get(self, hid):
		search = hid
		results = []
		# with open('ra_data_classifier.csv', 'rb') as csvfile:
		reader = csv.reader(open('ra_data_classifier.csv', "rb"), delimiter=",")
		# csv_file = csv.reader(open('ra_data_classifier.csv', "rb"), delimiter=",")
		# for row in reader:
		# 	if search == row[1]
		# 		results.append(row)
		# 		return jsonify(results)
		# return "Hid not found"

	def post(self, hid):
		search = hid
		csv_file = csv.reader(open('ra_data_classifier.csv', "rb"), delimiter=",")
		for row in csv_file:
			# if search == row[1]
			# 	out = open('ra_data_classifier.csv', "w")
			# 	for row in 1:
			# 		for column in row:
			# 			out.write('%d;' % column)
			# 		out.write('\n')
			# 	out.close()
		# parser = reqparse.RequestParser()
		# parser.add_argument("chunk")
		# parser.add_argument("has space")
		# args = parser.parse_args()

		# for user in datas:
		# 	if(hid == user["hid"]):
		# 		return "Hid already exists"
		# data = {
		# 	"hid": hid,
		# 	"chunk": args["chunk"],
		# 	"has space": args["has space"]
		# }
		# datas.append(data)
		# return data

api.add_resource(User, "/data/<string:hid>")
app.run(debug=True)
# class Hid(Resource):
# 	def get(self, hid):
# 			conn = csv_connect.connect()
# 			query = conn.execute("select * from data where hid = %d " %str(hid))
# 			result = {'data': [dict(zip(tuple(query.keys()),i)) for i in query.cursor]}
# 			return jsonify(result)

# api.add_resource(Hid_info, '/data/<hid>') # Route

# if __name__ == '__main__':
# 	app.run(port = '5002')