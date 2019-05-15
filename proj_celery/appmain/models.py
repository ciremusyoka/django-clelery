from django.db import models

class Example(models.Model):
    ans = models.FloatField(max_length=20)
