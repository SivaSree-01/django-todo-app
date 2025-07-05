from django.db import models

class Task(models.Model):
    Title = models.CharField(max_length=200)
    Completed = models.BooleanField(default=False)
    DueDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.Title