from django.shortcuts import render, redirect
from datetime import datetime
from kanban.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from kanban.forms import *
from django.http import HttpResponse
from django.db.utils import IntegrityError
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
        # breakpoint()
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

        return render(request,'kanban/cards.html', {'todo':todo, 'in_progress':inprogress, 'done':done,'on_hold':onhold,'name':name, 'kid':id})

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
            acess = hasAcessTo()
            acess.kanban = new_board
            acess.user = request.user
            acess.save()
            return redirect('kanban:home')
        else:
            return render(request, 'kanban/create_board.html', {'form': form})
    
@login_required
def add_card(request, kid, state):
    if request.method == 'GET':
        form = addCardForm()
        return render(request, 'kanban/add_card.html', {'form':form, 'error':""})
    else:
        form = addCardForm(request.POST)
        if form.is_valid():
            new_card = Cards()
            new_card.KanbanId = Kanban.objects.get(pk=kid)
            new_card.author = request.user
            new_card.cardID = form.cleaned_data['cardID']
            new_card.state = state
            new_card.last_edit = datetime.now()
            new_card.content = form.cleaned_data['content']
            new_card.deadline = form.cleaned_data['deadline']
            try:
                new_card.save()
                # created = creates()
                # created.card = new_card
                # created.KanbanId = Kanban.objects.get(pk=kid)
                # created.user = request.user
                # created.save()
                return redirect('kanban:kontent', id=kid)
            except IntegrityError:
                return render(request, 'kanban/add_card.html', {'form':form, 'error':"Card with this ID already exists, try a different ID"})    
        else:
            return render(request, 'kanban/add_card.html', {'form':form, 'error':""})

@login_required
def delete_card(request,kid,cid):
    Cards.objects.filter(KanbanId=kid).filter(cardID=cid).delete()
    return kontent(request, kid)

@login_required
def join_board(request):
    if request.method == 'GET':
        form = joinBoardForm()
        return render(request, 'kanban/join_board.html', {'form':form})
    else:
        form = joinBoardForm(request.POST)
        if form.is_valid():
            access = hasAcessTo()
            access.kanban = Kanban.objects.get(pk=form.cleaned_data['kanbanId'])
            access.user = request.user
            access.save()
            return redirect('kanban:home')
        else:
            return render(request, 'kanban/join_board.html', {'form':form})

@login_required
def move_card(request, kid, cid, state):
    card_objs = Cards.objects.filter(KanbanId=kid).filter(cardID=cid)
    card = card_objs[0]
    new_card = Cards()
    new_card.cardID = card.cardID
    new_card.KanbanId = card.KanbanId
    new_card.state = state
    new_card.author = request.user
    new_card.last_edit = datetime.now()
    new_card.deadline = card.deadline
    new_card.content = card.content
    card.delete()
    new_card.save()
    return redirect('kanban:kontent', id=kid)