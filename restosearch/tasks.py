from celery.decorators import task
from celery.utils.log import get_task_logger
from django.contrib.gis.geos import Point
from django.db.models import *
from restosearch.models import *
logger = get_task_logger(__name__)


@task(name="populatedb")
def populatedb(apidata,apiname,apiaddress,apicity,lat,lng):
	# print(lat,lng)
	loc=Point(float(lat),float(lng))
	if Restaurant.objects.filter(location__coveredby=loc).exists()==False:
		restos=Restaurant.objects.create(data=apidata,name=apiname,address=apiaddress,city=apicity,location=loc)
		# logger.info("created")
		restos.save()
	logger.info("created")

    # return send_feedback_email(email, message)
