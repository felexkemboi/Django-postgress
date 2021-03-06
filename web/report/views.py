from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Item,Board,Topic
#import function to open the url
from urllib.request import urlopen,Request

from django.contrib.auth import login, authenticate,logout,get_user_model
from django.contrib.auth.forms import UserCreationForm

from report.forms import SignUpForm,LoginForm,NewTopicForm


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

def allboard(request):
	boards = Board.objects.all()
	return render(request, 'allnoards.html',{"boards":boards})

def posts(request):
	posts = Post.objects.all()
	return render(request, 'allposts.html',{"posts":posts})

def topics(request):
	topics = Topic.objects.all()
	return render(request, 'alltopics.html',{"topics":topics})

def loginview(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get('password')
		user = authenticate(username = username,password=password)
		login(request,user)
		print(request.user.is_authenticated)
		return redirect('#')
	else:
		form = LoginForm()
	return render(request, 'login.html',{'form':form})
"""
def signup(request):
	form = (request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get('password')
		user = authenticate(username = username,password=password)
		login(request,user)
		print(request.user.is_authenticated)
	return render(request, 'signup.html',{})
"""
def logout(request):
	logout(request,user)
	return render(request, 'logout.html',{})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            #username =     form.cleaned_data.get('username')
            password =     form.cleaned_data.get('password')
            #email =        form.cleaned_data.get("email")
            #user = authenticate(username=username, password=raw_password)
            user.set_password(password)
            user.save()
            login(request,user)
            print(request.user.is_authenticated)
            #redirect('records')
            return redirect('nyumbani')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def input(request):
	return render(request, 'input.html',{})


def output(request):
	name = request.GET['name']
	phone = request.GET['phone']
	email = request.GET['email']
	message = request.GET['message']
	"""user = User.objects.create(
		name = name,
		phone = 
		)
	user.save()

	login(request,user)  """
	
	return render(request, 'output.html')

def nyumbani(request):
	return render(request, 'nyumbani.html',{})

def base1(request):
	return render(request, 'base1.html',{})

def alltopics_board(request, pk):
    board = get_object_or_404(Board, pk=pk)
    topics = Topic.objects.filter(board=board)
    print(topics)
    return render(request, 'topics.html',{'topics':topics})

"""
, {'board': board,'topics':topics}
def newtopic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'newtopic.html', {'board': board})
"""
   
#@login_required
def newtopic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user  # <- here
            topic.save()
            Topic.objects.create(
                message=form.cleaned_data.get('message'),
                subject=form.cleaned_data.get('subject'),
                board=board,                
                starter=request.user  # <- and here
            ).save()
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'newtopic.html', {'board': board, 'form': form})

"""
def topicflani(request,pk,board_pk,):
	<a href="{% url 'topic_posts' board.pk topic.pk %}">{{ topic.subject }}</a></td>

	topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
	topic.views += 1
	topic.save()
	return render(request, 'topic_posts.html', {'topic': topic})
	topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
	return render(request, 'topicflani.html',{'topic': topic})
	#topic = get_object_or_404(Topic, pk=board__pk, pk=topic_pk)
	board.pk topic.pk 
	"""

def topicflani(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    return render(request, 'topicflani.html', {'topic': topic})

def boardflani(request, pk):
    board = get_object_or_404(Board, pk=pk)
    topics = Topic.objects.filter(board=board)
    print(topics)
    return render(request, 'topics.html',{'topics':topics})
	