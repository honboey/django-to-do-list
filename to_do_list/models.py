from datetime import date

from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    deadline = models.DateField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def is_overdue(self):
        if self.deadline:
            return self.deadline < date.today()

