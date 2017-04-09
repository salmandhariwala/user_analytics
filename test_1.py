import mongo_aggregation_factory
import mongo_aggregation
import datetime
from flask import Flask, request, redirect, url_for, send_from_directory,Response,jsonify,json

start = datetime.datetime.fromtimestamp(1479369427)
end = datetime.datetime.fromtimestamp(1491724091)

query = mongo_aggregation_factory.get_user_activity_query(start,end,"none")
# print(query)

result = mongo_aggregation.perform_aggregateion(query)

print(json.dumps(result))

