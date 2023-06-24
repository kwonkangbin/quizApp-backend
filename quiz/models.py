from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_lenth = 200)
    body = models.TextField()
    answer = models.IntergerField()
