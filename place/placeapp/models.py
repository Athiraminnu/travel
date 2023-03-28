from django.db import models

# Create your models here.

class place2visit(models.Model):
    img = models.ImageField(upload_to='pic')
    name = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.name

