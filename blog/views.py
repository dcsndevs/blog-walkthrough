from django.shortcuts import render
from django.http import HttpResponse

# Create your views heres.
def my_blog(request):
    return HttpResponse('Hello Dickson')

def index(request):
    # Replace 'https://example.com' with the URL of the webpage you want to embed
    embedded_webpage_url = 'https://transecurehub.com/'

    # Create the HTML content with an <iframe> tag
    html_content = f'<iframe src="{embedded_webpage_url}" width="100%" height="100%"></iframe>'

    # Return the HttpResponse with the embedded webpage
    return HttpResponse(html_content)