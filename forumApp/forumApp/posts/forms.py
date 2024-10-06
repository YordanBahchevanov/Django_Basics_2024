from django import forms
from django.forms import formset_factory

from forumApp.posts.choices import LanguageChoice
from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        error_messages = {
            'title': {
                'required': 'Please enter the title of your post',
                'max_length': f'The title is too long. Please keep it under {Post.TITLE_MAX_LENGTH} characters'
            },
            'author': {
                'required': 'Please enter an author',
            }
        }


class PostCreateForm(PostForm):
    pass


class PostEditForm(PostForm):
    pass


class PostDeleteForm(PostForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...',
            }
        )
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'get'
    #     self.helper.form_class = 'form-inline'


# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#     )
#
#     content = forms.CharField(
#         widget=forms.Textarea,
#     )
#
#     author = forms.CharField(
#         max_length=30,
#     )
#
#     created_at = forms.DateTimeField()
#
#     languages = forms.ChoiceField(
#         choices=LanguageChoice.choices,
#     )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'author',
            'content',
        )

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'Author name is required!',
            },
            'content': {
                'required': 'Content is required!',
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add message...',
            'rows': 1,
        })


CommentFormSet = formset_factory(CommentForm, extra=1)
