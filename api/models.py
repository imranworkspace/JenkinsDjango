from django.db import models

# Create your models here.
class EmpModel(models.Model):
    ename=models.CharField(max_length=25)
    email=models.EmailField()

    def __str__(self):
        return self.ename