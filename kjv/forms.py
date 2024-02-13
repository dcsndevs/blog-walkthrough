from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    verse = forms.CharField(max_length=100, label="Bible Verse (e.g. John 3:16)")
