from django.db import models

# Create your models here.
class Thread(models.Model):
    subject = models.CharField(max_length=120)
    locked  = models.BooleanField(default=False)
    pinned  = models.BooleanField(default=False)
    archived= models.BooleanField(default=False)

class Post(models.Model):
    name        = models.CharField(blank=False, default='Anonymous', max_length=64)
    content     = models.TextField()
    hidden      = models.BooleanField(default=False)
    post_time   = models.DateTimeField(auto_now=True)
    ip          = models.CharField(null=True, max_length=24)
    hex_id      = models.CharField(null=True, max_length=6)
    thread      = models.ForeignKey(Thread, on_delete=models.CASCADE, null=True)
