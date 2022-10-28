from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    technology = models.CharField(max_length=32)
    image = models.FilePathField(path="/img")
    url = models.URLField(max_length=128)
    
    def __str__(self) -> str:
        return self.title