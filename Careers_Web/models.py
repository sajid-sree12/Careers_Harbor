from django.db import models

# Create your models here.






class Career_feedback(models.Model):
    feedback=models.CharField(max_length=100)
    fullname=models.CharField(max_length=30)
    email=models.EmailField()
    rating=models.IntegerField()
    status=models.CharField(default="pending",max_length=30)
    def __str__(self):
        return self.fullname