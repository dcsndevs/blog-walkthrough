from django.core.management.base import BaseCommand
import json
from bible_app.models import Book, Chapter, Verse

class Command(BaseCommand):
    help = 'Load Bible data from JSON files'

    def handle(self, *args, **kwargs):
        # Load book data
        with open('books_data.json') as f:
            books_data = json.load(f)['books']

        # Load Bible data
        with open('bible_data.json') as f:
            bible_data = json.load(f)

        # Populate Books table
        for book_info in books_data:
            Book.objects.create(name=book_info['name'], book_id=book_info['book_id'])

        # Populate Chapters and Verses tables
        for entry in bible_data:
            fields = entry['fields']
            book_id = fields['book_id']
            chapter_id = fields['chapter_id']
            verse_number = fields['verse_id']
            text = fields['text']

            book = Book.objects.get(book_id=book_id)
            chapter, _ = Chapter.objects.get_or_create(book=book, chapter_number=chapter_id)
            Verse.objects.create(chapter=chapter, verse_number=verse_number, text=text)

        self.stdout.write(self.style.SUCCESS('Bible data loaded successfully'))
