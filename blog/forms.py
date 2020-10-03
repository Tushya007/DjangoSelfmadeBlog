from django import forms
from .models import BlogModel 

class BlogCreateForm(forms.ModelForm):
    title = forms.CharField(label="Blog title",widget=forms.TextInput(attrs={
        "placeholder":"Your title here",
        "class":"col-12",
    }))
    content = forms.CharField(label="Blog content",widget=forms.Textarea(attrs={
        "placeholder":"Your blog content here",
        "class":"col-12",
    }))

    class Meta:
        model = BlogModel
        fields = [
            'title',
            'content'
        ]