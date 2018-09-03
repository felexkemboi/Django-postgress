from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
#import function to open the url
from urllib.request import urlopen,Request

"""
def home(request):
    return render(request, 'home.html')
"""



def home(request):
    boards = Board.objects.all() #fetch all records in the database and assign it to boards
    boards_names = list()  #declare an empty list

    for board in boards:                 #sasa wewe Hassan ni wewe utanieleza hii ya for loop
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)

def scrap(request):
	#import BeautifulSoup function
	from bs4 import BeautifulSoup as soup

	#url of the page to scrap the data from
	url = 'https://www.jumia.co.ke/tuskys-electronics/'

	#override the user-agent with Mozilla
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})


	#open up a connection  by grabbing  the page and assign it to a variable
	uClient = urlopen(req)
	page_html = uClient.read() #read the page in raw html
	uClient.close() #always close a file after reading from it


	page_soup = soup(page_html,"html.parser")

	#grab each product
	containers = page_soup.findAll("div",{"class":"sku -gallery"})

	for container in containers:
		brand    = container.find("span",{"class":"brand"}).text.strip()
		name     = container.find("span",{"class":"name"}).text.strip()
		myprices = container.find("span",{"class":"price-box ri"})
		newprice = myprices.find("span",{"class":"price"}).text.strip()
		oldprice = myprices.find("span",{"class":"price -old "}).text.strip()
		#print("Brand:" +brand "Name:" +name "New Price:" +newprice "Old Price:" + oldprice),{"brand": brand,"name" :name,"newprice":newprice,"oldprice":oldprice}
		obj,created = Item.objects.get_or_create(
             	name=name,
                brand=brand,
                newprice=newprice,
                oldprice=oldprice
            )
		print("Added a new record !")
		#try to understand the django behind obj,create   !!!!!!!!!!!!!!!!!
		#item.save()
		#data = Item.objects.all()
		#return redirect('a')
		"""
		for record in data:
			if item == record:
				print("Already added")
			else:
				item.save()
					,{"data":data}
				"""
	data = Item.objects.all()
	return render(request, 'home.html',{"data":data})

def records(request):
	data = Item.objects.all()
	return render(request, 'records.html',{"data":data})

