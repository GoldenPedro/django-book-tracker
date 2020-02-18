from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = Post
        fields = (
            'book_title',
            'book_author',
            'stars',
        )

