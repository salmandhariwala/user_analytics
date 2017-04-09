import pymongo
from pymongo import MongoClient

__mongo_host = "localhost"
__mongo_port = 27017
__mongo_user_analytics_db = "user_analytics"
__mongo_user_analytics_collection = "user_analytics"

def perform_aggregateion(pipeline):

	# get client
	client = MongoClient(__mongo_host, __mongo_port)

	# get db
	db = client[__mongo_user_analytics_db]

	# get collection
	collection = db[__mongo_user_analytics_db]

	# perform aggregation
	return list(collection.aggregate(pipeline))

	# close the connection
	client.close()