def get_query(start_time,end_time,entity):

	if entity == "user":
		return get_user_activity_query(start_time,end_time)
	elif entity == "dashboard":
		return get_dashboard_query(start_time,end_time)
	elif entity == "groupBy" :
		return get_group_query(start_time,end_time)
	elif entity == "filter" :
		return get_filter_query(start_time,end_time)
	elif entity == "login" :
		return get_login_query(start_time,end_time)				

def get_filter_query(start_time,end_time):
	query =[
	{"$match":{"message":"activate","client":"nezu","client":"nezu","logTime":{"$gte": start_time, "$lt": end_time}}},
	{"$unwind":"$masterFilter"},
	{"$group":{"_id":{"filterValue":"$masterFilter.values"},"filterCount":{"$sum":1}}},
	{"$project":{"entity":"$_id.filterValue","score":"$filterCount","_id":False}},
	{"$sort":{"score":-1}}]

	return query

def get_login_query(start_time,end_time):
	query =[
	{"$match":{"message":"activate","client":"nezu","logTime":{"$gte": start_time, "$lt": end_time}}},
	{"$group":{"_id":{"user":"$user"},"sessions":{"$addToSet":"$session"}}},
	{"$project":{"_id":False,"entity":"$_id.user","score":{"$size":"$sessions"}}},
	{"$sort":{"score":-1}}
	]

	return query

def get_dashboard_query(start_time,end_time):
	query = [
	{"$match":{"message":"activate","client":"nezu","logTime":{"$gte": start_time, "$lt": end_time}}},
	{"$unwind":"$widgets"},
	{"$group":{"_id":{"widgets":"$widgets"},"widgetCount":{"$sum":1}}},
	{"$project":{"entity":"$_id.widgets","score":"$widgetCount","_id":False}},
	{"$sort":{"score":-1}}
	]
	return query

def get_group_query(start_time,end_time):
	query = [
	{"$match":{"message":"activate","client":"nezu","logTime":{"$gte": start_time, "$lt": end_time}}},
	{"$unwind":"$groups"},
	{"$group":{"_id":{"groupBy":"$groups"},"groupByCount":{"$sum":1}}},
	{"$project":{"entity":"$_id.groupBy","score":"$groupByCount","_id":False}},
	{"$sort":{"score":-1}}
	]

	return query	

def get_user_activity_query(start_time,end_time):

	query = [
	{"$match":{"message":"activate","client":"nezu","logTime":{"$gte": start_time, "$lt": end_time}}},
	{"$group":{"_id":{"user":"$user"},"activateCount":{"$sum":1}}},
	{"$project":{"_id":False,"score":"$activateCount","entity":"$_id.user"}},
	{"$sort":{"score":-1}}
	]
	
	return query	

