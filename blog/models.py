from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_time_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)