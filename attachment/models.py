from django.db import models
from django.contrib.auth.models import User

class Attachment(models.Model):
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'
