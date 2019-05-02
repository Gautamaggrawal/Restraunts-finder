from urllib.error import URLError
from django.contrib.gis import geos
from django.contrib.gis import measure
from django.shortcuts import render_to_response
from django.contrib.gis.db.models.functions import Distance
from django.template import RequestContext
from geopy.geocoders.googlev3 import GoogleV3
from geopy.geocoders.googlev3 import GeocoderQueryError
from restosearch import forms
from restosearch import models
from django.shortcuts import render
from .utils import *
from django.conf import settings

def geocode_address(address):
    address = address.encode('utf-8')
    search(address)

    print('sss',search(address))
    geocoder = GoogleV3(api_key=settings.GOOGLE_MAP_API_KEY)
    try:
        _, latlon = geocoder.geocode(address)
    except (URLError, GeocoderQueryError, ValueError):
        return None
    else:
    	print(latlon)
    	return latlon

def get_Restaurants(longitude, latitude):
    current_point = geos.fromstr("POINT(%s %s)" % (longitude, latitude))
    distance_from_point = {'km': 10}
    print(current_point)
    Restaurants = models.Restaurant.objects.filter(location__distance_lte=(current_point, measure.D(**distance_from_point)))
    # print(models.Restaurant.objects.annotate(distance=Distance("location", current_point)).order_by("distance")[0:6])
    print(Restaurants)
    # Restaurants = Restaurants[0].location.distance(current_point).order_by('distance')
    # return Restaurants[0].distance(current_point)
    return models.Restaurant.objects.annotate(distance=Distance("location", current_point)).order_by("distance")[0:6].values()

def home(request):
    form = forms.AddressForm()
    Restaurants = []
    if request.POST:
        form = forms.AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            location = geocode_address(address)
            if location:
                latitude, longitude = location
                Restaurants = get_Restaurants(longitude, latitude)

    return render(request,
        'home.html',
        {'form': form, 'Restaurants': Restaurants})
