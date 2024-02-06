from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    phone = models.IntegerField()

    def __str__(self): # for getting the name of author in database/admin_panel
        return self.name
    