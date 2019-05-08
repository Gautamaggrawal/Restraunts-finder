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
from .utils import GetRestos
from django.conf import settings


def geocode_address(address):
    address = address.encode('utf-8')
    # search(address)
    geocoder = GoogleV3(api_key=settings.GOOGLE_MAP_API_KEY)
    try:
        _, latlon = geocoder.geocode(address)
    except (URLError, GeocoderQueryError, ValueError):
        return None
    else:
        print(latlon)
        return latlon


def get_Restaurants(longitude, latitude,radius):
    current_point = geos.fromstr("POINT(%s %s)" % (longitude, latitude))
    distance_from_point = {'km': radius}
    print(current_point)
    Restaurants = models.Restaurant.objects.filter(
        location__distance_lte=(current_point, measure.D(**distance_from_point)))
    # print(models.Restaurant.objects.annotate(distance=Distance("location", current_point)).order_by("distance")[0:6])
    print(Restaurants.count())
    # Restaurants = Restaurants[0].location.distance(current_point).order_by('distance')
    # return Restaurants[0].distance(current_point)
    return models.Restaurant.objects.annotate(distance=Distance("location", current_point)).order_by("distance").values()


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

def trys(request):
    return render(request,'base.html')
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import Point

@csrf_exempt
def search(request):
    if request.method=='POST':
        print(request.POST)
        lat = request.POST.getlist('lat')
        lng = request.POST.getlist('lng')
        radius = request.POST.getlist('radius')
        city = request.POST.getlist('city')
        print("dewdwedewdew",lat,lng)
        print("dewd",city)
        city=lng[2].split(",")[0]
        print(city)
        print("exists karta hai ya nahi",models.Restaurant.objects.filter(city__icontains=city).exists())
        if models.Restaurant.objects.filter(city__icontains=city).exists()==False:
            GetRestos.searchapi(lng[2])
        radius=float(lng[1])
        lat,lng=lat[0],lng[0]

        point = Point(float(lng),float(lat))
        restos=get_Restaurants(float(lat),float(lng),radius)
        # restos = models.Restaurant.objects.filter(location__distance_lte=(point, measure.D(m=radius))).values()
        # print("res",restos)
        return JsonResponse({'data': "s"})


        return render(request,'home.html',{'rest':restos})
