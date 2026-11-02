from django.db import models

class Project(models.Model):
    rodun = models.IntegerField()  # 0) röðun
    fyrirsogn = models.CharField(max_length=200, blank=True)  # 1)
    texti1 = models.TextField(blank=True)  # 2)
    texti2 = models.TextField(blank=True)  # 3)
    texti3 = models.TextField(blank=True)  # 4)
    image1 = models.ImageField(upload_to='verkefni/', blank=True, null=True)  # 5)
    image2 = models.ImageField(upload_to='verkefni/', blank=True, null=True)  # 6)
    image3 = models.ImageField(upload_to='verkefni/', blank=True, null=True)  # 7)
    image4 = models.ImageField(upload_to='verkefni/', blank=True, null=True)  # 8)
    image5 = models.ImageField(upload_to='verkefni/', blank=True, null=True)  # 9)
    image6 = models.ImageField(upload_to='verkefni/', blank=True, null=True)  # 10)

    def __str__(self):
        return self.fyrirsogn or f"Verkefni #{self.pk}"
# Create your models here.
