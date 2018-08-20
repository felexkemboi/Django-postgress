from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


def home(request):
    return render(request, 'home.html')




def home(request):
    boards = Board.objects.all() #fetch all records in the database and assign it to boards
    boards_names = list()  #declare an empty list

    for board in boards:                 #sasa wewe Hassan ni wewe utanieleza hii ya for loop
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)