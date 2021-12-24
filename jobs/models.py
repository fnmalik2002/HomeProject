from django.db import models
from django.db.models.deletion import CASCADE
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class JobPost(models.Model):
    job_title = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')
    job_detail = models.CharField(max_length=200)
    job_price = models.IntegerField(default=0)
    job_taken = models.BooleanField(default=False)
    job_done = models.BooleanField(default=False)
    job_done_date = models.DateTimeField('date job completed', null=True, blank=True)
    job_taker = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='job_user')
    job_creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='job_author')
    def __str__(self):
        return self.job_title
    
    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)

class Payments(models.Model):
    jobpost = models.ForeignKey(JobPost, on_delete=CASCADE)
    payment_for_month = models.CharField(max_length=200)
    payment_amount = models.IntegerField(default=0)
    payment_date = models.DateTimeField('payment date')

    def __str__(self):
        return self.job_detail
