from django.forms import ModelForm
from .models import Post

class create_post(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title','content',
        ]
        