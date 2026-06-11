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


class ProjectReview(models.Model):
    REVIEW_STATUS = (
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='project_reviews')
    status = models.CharField(max_length=20, choices=REVIEW_STATUS)
    reason = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-reviewed_at']

    def __str__(self):
        return f"{self.project.title} - {self.status}"