from django.db import models
from django.contrib.auth.models import User


class Kanban(models.Model):
    description = models.CharField(max_length=1000)
    KanbanName = models.CharField(max_length=200)
    KanbanId = models.IntegerField(unique=True, primary_key=True)


class Cards(models.Model):

    cardID = models.IntegerField()
    KanbanId = models.ForeignKey(Kanban, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    state = models.TextField(max_length=200)
    last_edit = models.DateTimeField()
    content = models.TextField(max_length=1000)
    deadline = models.DateTimeField()
    class Meta:
        unique_together = (('cardID', 'KanbanId'))

class creates(models.Model):
    card = models.ForeignKey(Cards, on_delete=models.PROTECT)
    KanbanId = models.ForeignKey(Kanban, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class hasAcessTo(models.Model):
    kanban = models.ForeignKey(Kanban, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

# class contains(models.Model):
