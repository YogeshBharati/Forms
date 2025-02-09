from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    interested_course = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    