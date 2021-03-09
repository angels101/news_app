from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class entry(models.Model):
    entry_title = models.CharField(max_length=50)
    entry_text = models.TextField()
    entry_data = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User,on_delete=models.CASCADE)