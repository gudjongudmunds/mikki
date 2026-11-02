from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    education = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='staff_images/')

    def __str__(self):
        return self.name