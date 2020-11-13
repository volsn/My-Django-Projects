from django.db import models

# Create your models here.

class Preorder(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    birthdate = models.DateField()

    def __str__(self):
        return self.name