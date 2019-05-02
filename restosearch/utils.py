import requests
from django.contrib.gis.geos import Point
from django.conf import settings
# pnt = Point(5, 23)
def search(QUERY):
	EP = 'https://developers.zomato.com/api/v2.1/{}' # endpoint for Zomato
	HEADER = {'user-key': settings.ZOMATO_API_KEY}
	r = requests.get(EP.format('categories'), headers=HEADER)
	categories = r.json()
	# print(categories)
	r = requests.get(EP.format('locations'), headers=HEADER, params={'query': QUERY})
	location = r.json()
	# print(QUERY in location['location_suggestions'][0]['title'])
	# print(location['location_suggestions'][0]['title'])
	found=''
	# if location['has_total']>=1:
	# 	found=location['location_suggestions'][0]['title']
	
	# if QUERY!=found or location['has_total']==0:
	# 	url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+{}&key={}'
	# 	r=requests.get(url.format(QUERY,settings.GOOGLE_MAP_API_KEY))
	# 	restos=r.json()['results']
	# 	for i in restos:
	# 		print(i['name'])
	# 		print(i['formatted_address'])
	# 		print(i['geometry']['location'])
	# 		# print(i)
	# else:
	for i in categories['categories']:
		for l in location['location_suggestions']:
			param = {'entity_id': l['entity_id'],'entity_type': l['entity_type'],'category': i['categories']['id']}
			r = requests.get(EP.format('search'), headers=HEADER, params=param)
			rest = r.json()
			print(rest)

			for loc in rest['restaurants']:
				# loc = loc['restaurant']
				# print(loc)
				pass

#search("delhi")