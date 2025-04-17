from django.db import models

class SubTask(models.Model):
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Sub Task'
        verbose_name_plural = 'Sub Tasks'
