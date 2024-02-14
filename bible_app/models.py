from django.db import models


# Create your models here.    
class Book(models.Model):
    name = models.CharField(max_length=100)
    book_id = models.IntegerField(unique=True)

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()

class Verse(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    verse_number = models.IntegerField()
    text = models.TextField()

    class Meta:
        unique_together = ('chapter', 'verse_number')