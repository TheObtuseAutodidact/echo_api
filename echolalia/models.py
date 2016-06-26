from django.db import models

# Create your models here.
class Echo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.message
