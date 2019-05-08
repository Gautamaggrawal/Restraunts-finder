from celery.decorators import task
from celery.utils.log import get_task_logger
from django.contrib.gis.geos import Point
# pnt = 
from restosearch.models import *
logger = get_task_logger(__name__)


@task(name="populatedb")
def populatedb(apidata,apiname,apiaddress,apicity,lat,lng):
	loc=Point(float(lat),float(lng))
	print(loc)
	rest=Restaurant.objects.create(data=apidata,name=apiname,address=apiaddress,city=apicity,location=loc)
	rest.save()
	logger.info("DB populated")
    # return send_feedback_email(email, message)
