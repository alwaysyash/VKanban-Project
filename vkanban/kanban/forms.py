from django import forms
from django.forms import ModelForm
from kanban.models import *

class creatBoardForm(ModelForm):
    class Meta:
        model = Kanban
        fields = ['KanbanId','KanbanName','description']
        
class addCardForm(ModelForm):
    class Meta:
        model = Cards
        fields = ['cardID','content', 'deadline']

class joinBoardForm(forms.Form):
    kanbanId = forms.IntegerField()