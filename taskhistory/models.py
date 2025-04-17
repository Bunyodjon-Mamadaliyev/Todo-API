from django.db import models
from django.contrib.auth.models import User

class TaskHistory(models.Model):
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.task.title}"
