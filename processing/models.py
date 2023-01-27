from django.db import models


class DataPost(models.Model):
    content = models.FileField()
