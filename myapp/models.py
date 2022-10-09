from django.db import models

# Create your models here.
class FormInfo(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.TextField()
    message=models.TextField()

    def __str__(self):
        return self.name

class Resume(models.Model):
    file=models.FileField()