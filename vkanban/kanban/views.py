from django.shortcuts import render
from datetime import datetime
from kanban.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from kanban.forms import *
from django.http import HttpResponse
# Create your views here.
@login_required
def home(request):
    # breakpoint()
    if(request.method == "GET"):
        boards = hasAcessTo.objects.filter(user = request.user)
        context = []
        for i  in boards:
            d = dict()
            d['id'] = i.kanban.KanbanId
            d['name'] = i.kanban.KanbanName
            d['description'] = i.kanban.description
            context.append(d)
        return render(request, 'kanban/boards.html', {'boards':context})
    else:
        return None

@login_required
def kontent(request, id):
    if(request.method == "GET"):
        cards = Cards.objects.filter(KanbanId=id)
        name = Kanban.objects.get(pk=id).KanbanName
        states = ['todo', 'done','inprogress','onhold']
        todo = []
        inprogress = []
        done = []
        onhold = []
        for i in cards:
            d = dict()
            d['author'] = i.author.username
            d['content'] = i.content
            d['deadline'] = i.deadline
            d['state'] = i.state
            d['cardID'] = i.cardID
            d['last_edit'] = i.last_edit
            if(i.state=="todo"):
                todo.append(d)
            elif(i.state=="in_progress"):
                inprogress.append(d)
            elif(i.state=="done"):
                done.append(d)
            elif(i.state=="on_hold"):
                onhold.append(d)

        return render(request,'kanban/cards.html', {'todo':todo, 'in_progress':inprogress, 'done':done,'on_hold':onhold,'name':name})

@login_required
def create_board(request):
    if request.method == 'GET':
        form = creatBoardForm()
        return render(request, 'kanban/create_board.html',{'form':form})
    else:
        form = creatBoardForm(request.POST)
        if form.is_valid():
            new_board = Kanban()
            new_board.KanbanId = form.cleaned_data['KanbanId']
            new_board.KanbanName = form.cleaned_data['KanbanName']
            new_board.description = form.cleaned_data['description']
            new_board.save()
            return HttpResponse("New board added")
        else:
            return render(request, 'kanban/create_board.html', {'form': form})

