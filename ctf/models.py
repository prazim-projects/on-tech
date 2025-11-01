from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=100)
    points = models.IntegerField()
    flag = models.CharField(max_length=255) # The secret flag

    def __str__(self):
        return self.name

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    submitted_flag = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)

    class Meta: 
        unique_together = ('user', 'challenge') # A user can only solve a challenge once

    def __str__(self):
        return f"{self.user.username} - {self.challenge.name} ({'Correct' if self.is_correct else 'Incorrect'})"