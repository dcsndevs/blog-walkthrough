import requests
from django.shortcuts import render
from .forms import PostForm
from .models import PostScriptures

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            verse = form.cleaned_data['verse']
            
            # Make request to Bible API
            api_url = f'https://bible-api.com/{verse}'
            response = requests.get(api_url)
            if response.status_code == 200:
                passage = response.json()['text']
                return render(request, 'post_created.html', {'title': title, 'verse': verse, 'passage': passage})
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


# def view_verse(request, scripture):
#     # Make request to Bible API
#     api_url = f'https://bible-api.com/{scripture}?translation=kjv'
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         verse = response.json()['id', 'text']
#         return render(request, 'view_verse.html', {'verse': verse})
#     else:
#         return render(request, 'view_verse.html', {'error': 'Verse not found'})

def view_verse(request, scripture):
    # Make request to Bible API with KJV translation and verse numbers
    api_url = f'https://bible-api.com/{scripture}?translation=kjv&verse_numbers=true'
    response = requests.get(api_url)
    if response.status_code == 200:
        verse_data = response.json()
        book_name = verse_data['verses'][0]['book_name']
        chapter = verse_data['verses'][0]['chapter']
        verses = verse_data['verses']
        verse_text = "\n".join([f"{verse['verse']}. {verse['text']}" for verse in verses])
        return render(request, 'view_verse.html', {'book_name': book_name, 'chapter': chapter, 'verse_text': verse_text})
    else:
        return render(request, 'view_verse.html', {'error': 'Verse not found'})


def kjv_post_list(request):
    posts = PostScriptures.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
