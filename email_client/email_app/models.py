from django.db import models

# Create your models here.
class Email(models.Model):
    sent_to = models.CharField(max_length=200)
    sent_from = models.CharField(max_length=200)
    send_date = models.DateTimeField('date recieved/sent')
    subject = models.CharField(max_length=200)
    body = models.TextField()
    archived = models.PositiveSmallIntegerField(default=0) # 1 for archived 0 for not (duh)