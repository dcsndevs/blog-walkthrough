# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Book, Chapter, Verse

# def index(request):
#     return render(request, 'index.html')

# def get_books(request):
#     books = Book.objects.values('id', 'name')
#     return JsonResponse(list(books), safe=False)

# def get_chapters(request):
#     book_id = request.GET.get('book_id')
#     chapters = Chapter.objects.filter(book_id=book_id).values('chapter_number')
#     return JsonResponse(list(chapters), safe=False)

# def get_verses(request):
#     book_id = request.GET.get('book_id')
#     chapter_number = request.GET.get('chapter_number')
#     verses = Verse.objects.filter(chapter__book_id=book_id, chapter__chapter_number=chapter_number).values('verse_number', 'text')
#     return JsonResponse(list(verses), safe=False)

# views.py
from django.shortcuts import render
from .models import Book, Chapter, Verse

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def get_chapters(request):
    book_id = request.GET.get('book_id')
    chapters = Chapter.objects.filter(book_id=book_id)
    return render(request, 'chapters_dropdown.html', {'chapters': chapters})

def get_verses(request):
    book_id = request.GET.get('book_id')
    chapter_number = request.GET.get('chapter_number')
    verses = Verse.objects.filter(chapter__book_id=book_id, chapter__chapter_number=chapter_number)
    return render(request, 'verses_dropdown.html', {'verses': verses})
