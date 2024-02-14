from django import forms
from django.contrib import admin
from .models import PostScriptures


# Register your models here.
# admin.site.register(PostScriptures)

class PostScripturesAdminForm(forms.ModelForm):
    class Meta:
        model = PostScriptures
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        your_field_data = cleaned_data.get('scripture_reference')  # Replace 'your_field_name' with the actual name of your field
        if your_field_data:
            import re
            pattern = re.compile(r'^[A-Za-z]+\s\d+(:\d+)?$')
            if not pattern.match(your_field_data):
                raise forms.ValidationError("Please enter the data in the format 'John 3' or 'John 3:16'.")

        return cleaned_data

class PostScripturesAdmin(admin.ModelAdmin):
    form = PostScripturesAdminForm

admin.site.register(PostScriptures, PostScripturesAdmin)