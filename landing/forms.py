from django import forms


from .models import Post


class PostForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            "title",
            "preview_content",
            "content",
            "image",
            "draft",
            "publish",
        ]
