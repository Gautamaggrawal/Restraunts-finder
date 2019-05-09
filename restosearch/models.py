from urllib.error import URLError
from django.conf import settings
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from django.db import models
from geopy.geocoders.googlev3 import GoogleV3
from geopy.geocoders.googlev3 import GeocoderQueryError
from django.contrib.postgres.fields import JSONField

# from geopy import geocoders


class Restaurant(models.Model):
    website=models.CharField(max_length=20,null=True)
    data=JSONField(null=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=500)
    location = gis_models.PointField(u"longitude/latitude",
                                     geography=True, blank=True, null=True)

    # gis = gis_models.GeoManager()
    objects = models.Manager()

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.location:
            address = u'%s %s' % (self.city, self.address)
            address = address.encode('utf-8')
            geocoder = GoogleV3(api_key=settings.GOOGLE_MAP_API_KEY)
            try:
                _, latlon = geocoder.geocode(address)
            except (URLError, GeocoderQueryError, ValueError):
                pass
            else:
                point = "POINT(%s %s)" % (latlon[1], latlon[0])
                self.location = geos.fromstr(point)
        super(Restaurant, self).save()