# Restraunts-finder


[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2-brightgreen.svg)](https://djangoproject.com)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

## Functionality:
* Searches Restaurants in notime
* Locate Nearby Restaurants
* Calculate the distance from your location to the desired location 

## Introduction
**Restaurants Finder helps you decide where to have eat food by  picking a restaurant in your area. Open the website and desired location to get a random restaurant nearby. Press on the walking distance information at the bottom to open the location in Google Maps, or tap the refresh button at the top right to get another suggestion.**

## Technology
**The web app is build with GeoDjango. Styles are written in plain CSS and Bootstrap.Restaurants searches are powered with infinte scroll and AJAX to make provide Good User Experience 
The site is hosted on AWS and deployed with Gunicorn and Ngnix.**

**In order to get restaurant details Zomato  and Google Maps APIs  are used and to get the restraunts near a place Geospatial is used that gets stored in database in Background when user searches any city.The background task are accomplished by a Task Queue and Message Broker i.e CELERY and REDIS.**

http://restosfinder.ml

## Installation
Use redis [Redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04how-to-install-elasticsearch-logstash-and-kibana-elastic-stack-on-ubuntu-18-04)
Use postgresql [postgresql](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04).
setup posis [posis](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postgis-on-ubuntu-14-04).
Use the package manager [PIP3](https://pip.pypa.io/en/stable/).

```bash
install gdal-bin libgdal-dev
install python3-gdal
install binutils libproj-dev
```
**To setup the project on your local machine:**

1. Click on `Fork`.
2. Go to your fork and `clone` the project to your local machine.
3. `git clone https://github.com/Gautamaggrawal/Restraunts-finder.git`
4. Install the requirements `pip install -r requirements.txt`
5. Finally, run the development server `python manage.py runserver`

### Secret Key

Create and activate the Google Maps JavaScript API, which generates a API key. Copy this key in ```settings.py``` file in place of google-app-secret-key .

```GOOGLE_MAP_API_KEY = "google-app-secret-key"```
```ZOMATO_API_KEY = "zomato-secret-key"```


The project will be available at **127.0.0.1:8000**.


**To contribute to the project:**

1. Choose any open issue from [here](https://github.com/Gautamaggrawal/Restraunts-finder). 
2. Comment on the issue: `Can I work on this?` and get assigned.
3. Make changes to your fork and send a PR.

**To create a PR:**

Follow the given link to make a successful and valid PR: https://help.github.com/articles/creating-a-pull-request/

**To send a PR, follow these rules carefully,**otherwise your PR will be closed**:**

1. Make PR title in this format: `Fixes #IssueNo : Name of Issue`

For any doubts related to the issues, i.e., to understand the issue better etc, comment down your queries on the respective issue.

