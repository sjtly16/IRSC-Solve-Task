from django.db import models

class Schedule(models.Model):
    time = models.DateTimeField()
    url = models.URLField()
    
    def __str__(self):
        return self.time
