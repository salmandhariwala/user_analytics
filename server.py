from flask import Flask, request, redirect, url_for, send_from_directory,Response,jsonify,json
import os 
import DemoModule
import mongo_aggregation_factory
import mongo_aggregation
import datetime
import data

# Setup Flask app.
app = Flask(__name__)
app.debug = True


# this is for index.html file
@app.route('/')
def root():
  return app.send_static_file('index.html')

# this is for handling static contents
@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

# this is sample post method
@app.route('/test/post', methods=['POST'])
def sample_post():

	# access request post body
	print(request.data)

	# access request post headers
	print(request.headers)

	# access post data as dict
	mydict = request.get_json()

	# set reponse code
	res = Response(status=200)

	# set application type
	res.headers['Content-Type'] = "application/json"

	# get data
	# start = datetime.datetime.fromtimestamp(1479369427)								
	# end = datetime.datetime.fromtimestamp(1491724091)
	# entity = "user"

	# get data
	# start = datetime.datetime.fromtimestamp(1472757600)								
	# end = datetime.datetime.fromtimestamp(1491767400)
	# entity = "user"

	start = datetime.datetime.fromtimestamp(mydict["start_time"])
	end = datetime.datetime.fromtimestamp(mydict["end_time"])
	entity = mydict["entity"]

	print("params : {} {} {}".format(start,end,entity))

	my_data = data.fetch_data(start,end,entity)

	res.set_data(json.dumps(my_data))

	# return response
	return res 

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
  	app.run(host='0.0.0.0', port=port)