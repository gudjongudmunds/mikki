from django.db import models

class Inquiry(models.Model):
    submitted_at = models.DateTimeField(auto_now_add=True)  # Field 1
    name = models.CharField(max_length=100)                 # Field 2
    email = models.EmailField()                             # Field 3
    phone = models.CharField(max_length=20)                 # Field 4
    message = models.TextField()                            # Field 5

    def __str__(self):
        return f"Inquiry from {self.name} at {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
# Create your models here.
