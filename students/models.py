from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    marks = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-marks']

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
