import mongo_aggregation_factory
import mongo_aggregation
import datetime
from flask import Flask, request, redirect, url_for, send_from_directory,Response,jsonify,json

def fetch_data(start_time,end_time,entity):
	query = mongo_aggregation_factory.get_query(start_time,end_time,entity)
	result = mongo_aggregation.perform_aggregateion(query)

	return result



	