from django.db import models

# Create your models here.
class Information (models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField(blank=False,null=False)
    age=models.IntegerField(blank=False,null=False)
    dept=models.CharField(max_length=50)
    join_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    