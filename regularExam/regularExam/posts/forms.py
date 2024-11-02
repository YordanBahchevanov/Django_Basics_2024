from django import forms

from regularExam.mixins import ReadOnlyMixin
from regularExam.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['updated_at', 'author']


class PostCreateForm(PostBaseForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Put an attractive and unique title...",
        }),
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': "Share some interesting facts about your adorable pets...",
        }),
    )


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    readonly_fields = ['__all__']

