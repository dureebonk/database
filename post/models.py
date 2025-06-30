from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    pub_at = models.DateTimeField(auto_now=True)
    pub_by = models.ForeignKey(User, on_delete=models.CASCADE)

