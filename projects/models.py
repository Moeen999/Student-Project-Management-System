from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title