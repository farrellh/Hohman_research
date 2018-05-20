from flask import Flask
from flask_restful import Resource, Api, reqparse

# from sqlalchemy import create_engine
# from json import dumps
# from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///ra_data_classifier.csv')
app = Flask(__name__)
api = Api(app)

datas = [
	{
		"hid": "33BFF6QPI1YEFYISIWWDVQKGH8RW3Z",
		"chunk": "Landmark Center, 8th Fl",
		"has space": 0
	},
	{
		"hid": "3HUR21WDDUCUK1K6HMLPN3U0ZBSYX0",
		"chunk": "Contact: The C3 team at MakemeC3@cic.us -- Additional information at www.cambridgecoworking.com.",
		"has space": 0
	}
]

class User(Resource):
	def get(self, hid):
		for user in datas:
			if(hid == user["hid"]):
				return user
		return "Hid not found"

	def post(self, hid):
		parser = reqparse.RequestParser()
		parser.add_argument("chunk")
		parser.add_argument("has space")
		args = parser.parse_args()

		for user in datas:
			if(hid == user["hid"]):
				return "Hid already exists"
		data = {
			"hid": hid,
			"chunk": args["chunk"],
			"has space": args["has space"]
		}
		datas.append(data)
		return data

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