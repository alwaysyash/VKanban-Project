from django.shortcuts import render
from datetime import datetime
from kanban.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
