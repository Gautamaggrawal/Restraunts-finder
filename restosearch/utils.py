import requests
from django.conf import settings
from restosearch.tasks import populatedb
from celery.result import AsyncResult


class GetRestos:

    def searchzomapi(QUERY,start=0,count=20):
        EP = 'https://developers.zomato.com/api/v2.1/{}'  # endpoint for Zomato
        HEADER = {'user-key': "c3d3366545336bba3bcec47786f44130"}
        r = requests.get(EP.format('categories'), headers=HEADER)
        categories = r.json()
        r = requests.get(EP.format('locations'),
                         headers=HEADER, params={'query': QUERY})
        location = r.json()
        # print(location)
        lst = []
        print(location)
       	l=location['location_suggestions'][0]
        param = {'entity_id': l['entity_id'],
                 'entity_type': l['entity_type'],"start":start,"count":count}
        r = requests.get(EP.format('search'), headers=HEADER, params=param)
        rest = r.json()
        lst.append(rest)
        for loc in rest['restaurants']:
        	loc=loc['restaurant']
        	pppp=populatedb.delay('zomato',loc, loc['name'], loc['location']['address'],loc['location']['city'], loc['location']['latitude'],loc['location']['longitude'])
        	print("db populated?",pppp)        
        return lst

    def searchgoogleapi(QUERY):
        url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+{}&key={}'
        r=requests.get(url.format(QUERY,'AIzaSyAz0lOpBpL_AwqSHDVfPepRpaBG9-4u5Jg'))
        # print(r.json())
        lst=[]
        restos=r.json()['results']
        # print(restos)
        print(restos)
        lst.append(restos)
        for i in restos:
            # print(i)
            # # print(i['name'])
            # # print(i['formatted_address'])
            # print(i['geometry']['location']['lat'])
            # print(i['geometry']['location']['lng'])
            task=populatedb.delay('googlemaps',i, i['name'], i['formatted_address'],'', i['geometry']['location']['lat'],i['geometry']['location']['lng'])
            print(task.AsyncResult(task.request.id).state)
        return lst 
