from django.db import models

# Create your models here.
class PostScriptures(models.Model):
    title = models.CharField(max_length=100)
    # verse = models.CharField(max_length=100)  # Assuming verse format like "John 3:16"
    scripture_reference = models.CharField(max_length=100)
    
    def __str__(self):
        return self.scripture_reference