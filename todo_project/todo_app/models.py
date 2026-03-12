from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model) : 
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    description=models.TextField(max_length=500)
    isCompleted=models.BooleanField(default=False) 
    createdAt = models.DateTimeField(auto_now_add=True)
