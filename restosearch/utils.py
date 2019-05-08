# import requests
# from django.contrib.gis.geos import Point
# from django.conf import settings
# # pnt = Point(5, 23)
# class GetRestos:	
# 	def searchapi(QUERY):
# 		EP = 'https://developers.zomato.com/api/v2.1/{}' # endpoint for Zomato
# 		HEADER = {'user-key': "ec7629c2b4cd5c106bb63c6c15aded06"}
# 		r = requests.get(EP.format('categories'), headers=HEADER)
# 		categories = r.json()
# 		# print(categories)
# 		r = requests.get(EP.format('cities'), headers=HEADER, params={'q': QUERY})
# 		# print(r)
# 		location = r.json()
# 		print(location)
# 		if len(location['location_suggestions'])!= 0:
# 			# print(QUERY in location['location_suggestions'][0]['title'])
# 			# print(location['location_suggestions'][0]['title'])
# 			found=''
# 			# if location['has_total']>=1:
# 			# 	found=location['location_suggestions'][0]['title']
			
# 			# else:
# 			for i in categories['categories']:
# 				# print("it is i"+i)
# 				for l in location['location_suggestions']:
# 					param = {'entity_id': l['entity_id'],'entity_type': l['entity_type'],'category': i['categories']['id']}
# 					r = requests.get(EP.format('search'), headers=HEADER, params=param)
# 					rest = r.json()
# 					print(rest)

# 					for loc in rest['restaurants']:
# 						# loc = loc['restaurant']
# 						# print(loc)
# 						pass
# 		else:
# 			print("alalalalalal")		
# 			# if QUERY!=found or location['has_total']==0:
# 			url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+{}&key={}'
# 			r=requests.get(url.format(QUERY,"AIzaSyAz0lOpBpL_AwqSHDVfPepRpaBG9-4u5Jg"))
# 			restos=r.json()['results']
# 			for i in restos:
# 				print(i['name'])
# 				print(i['formatted_address'])
# 				print(i['geometry']['location'])
# 				print(i)


# # GetRestos.searchapi("Guna")


import requests
from django.conf import settings
from restosearch.tasks import populatedb
class GetRestos:

	def searchapi(QUERY):
	    EP = 'https://developers.zomato.com/api/v2.1/{}'  # endpoint for Zomato
	    HEADER = {'user-key': settings.ZOMATO_API_KEY}
	    r = requests.get(EP.format('categories'), headers=HEADER)
	    categories = r.json()
	    # print(categories)
	    r = requests.get(EP.format('locations'), headers=HEADER,
	                     params={'query': QUERY})
	    location = r.json()
	    # print(QUERY in location['location_suggestions'][0]['title'])
	    # print(location['location_suggestions'][0]['title'])
	    found = ''
	    # if location['has_total']>=1:
	    # 	found=location['location_suggestions'][0]['title']
	    # if QUERY!=found or location['has_total']==0:
		# url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+{}&key={}'
		# r=requests.get(url.format(QUERY,settings.GOOGLE_MAP_API_KEY))
		# restos=r.json()['results']
		# for i in restos:
		# 	print(i)
			# print(i['name'])
			# print(i['formatted_address'])
			# print(i['geometry']['location'])
	    		# print(i)
	    # else:	
	    for i in categories['categories']:
	        for l in location['location_suggestions']:
	            param = {'entity_id': l['entity_id'],
	                     'entity_type': l['entity_type'], 'category': i['categories']['id']}
	            r = requests.get(EP.format('search'), headers=HEADER, params=param)
	            rest = r.json()
	            # print(rest)

	            for loc in rest['restaurants']:
	                loc = loc['restaurant']
	                # print(loc['name'])
	                # # print(loc['featured_image'])
	                # # user_rating
	                # # cuisines
	                # # featured_image
	                # # photos_url
	                # # menu_url
	                # print(loc['location']['address'])
	                # print(loc['location']['city'])
	                # print(loc['location']['longitude'])
	                # print(loc['location']['longitude'])
	                populatedb.delay(loc, loc['name'], loc['location']['address'],
	                                 loc['location']['city'], loc['location']['latitude'],loc['location']['longitude'])
	                # pass

# GetRestos.searchapi("delhi")
