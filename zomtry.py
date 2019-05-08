import requests


zomato_api = '2bfbc4c07e842a726a76cb88d72429c4'


def get_location_details(query):

    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }
    params = (
        ('query', query),
    )

    response = requests.get('https://developers.zomato.com/api/v2.1/locations', headers=headers, params=params)
    data = response.json()

    for loc in data['location_suggestions']:
        loc_id = loc['entity_id']
        loc_type = loc['entity_type']

    return loc_id, loc_type


def get_restaurants(ent_id, ent_type):

    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }

    params = (
        ('entity_id', ent_id),
        ('entity_type', ent_type),
    )

    response = requests.get('https://developers.zomato.com/api/v2.1/search', headers=headers, params=params)

    return response.json()


if __name__ == '__main__':

    prompt = '> '
    print('Enter location to search')
    q = input(prompt)
    print()

    entity_id, entity_type = get_location_details(q)
    data = get_restaurants(entity_id, entity_type)

    print("Restaurants in " + q.title() + " --\n")

    for restaurant in data['restaurants']:
        r = restaurant['restaurant']
        print(r['name'].upper())
        loc = r['location']
        print(loc['locality'])
        rating = r['user_rating']
        print("Rating - " + str(rating['aggregate_rating']))

        print()
