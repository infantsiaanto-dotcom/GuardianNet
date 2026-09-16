from django.db import models
from django.contrib.auth.models import User
class Incident(models.Model):
    Category_choices = [
        ('Cyberbullying', 'Cyberbullying'),
        ('Phishing', 'Phishing'),
        ('Fake Profile', 'Fake Profile'),
        ('Harassment', 'Harassment'),
        ('Scam', 'Scam'),
        ('Other', 'Other'),
    ]
    Priority_choices = [
         ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    Status_choices = [
         ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=Category_choices)
    priority = models.CharField(max_length=10, choices=Priority_choices)
    status = models.CharField(max_length=20, choices=Status_choices, default='Pending')
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_details = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



