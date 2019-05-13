from restosearch.models import ZomatoCountry, ZomatoCity


class Validate:
    def Zomotocity(city='mzn', country='india'):
        zom_country = ZomatoCountry.objects.filter(country__iexact=country)
        if zom_country.exists():
            if ZomatoCity.objects.filter(city__icontains=city).exists():
            	print("aaaaaaaaaaaa",ZomatoCity.objects.filter(city__icontains=city).exists())
            	return True
            return False


# from bs4 import BeautifulSoup
# import requests
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# response = k=requests.get("https://www.zomato.com/cities",headers=headers)
# content = response.content
# soup = BeautifulSoup(content,"html.parser")
# k=0

# for i in soup.find_all("div",attrs={"class": "selected"}):
# 	for j in i.find_all("h1",attrs={"class":"home-cnd-con-name mb5"}):
# 		print(j.text)
# 		cntry=ZomatoCountry.objects.create(country=j.text.strip())
# 		for k in i.findNextSibling():
# 			print(k.text)
# 			ZomatoCity.objects.create(country=cntry,city=k.text.strip())				




