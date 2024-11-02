from django import forms

from regularExam.author.models import Author
from regularExam.mixins import ReadOnlyMixin


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorCreateForm(AuthorBaseForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Enter your first name...",
        }),
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Enter your last name...",
        }),
    )

    passcode = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': "Enter 6 digits...",
        }),
    )

    pets_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': "Enter the number of your pets...",
        }),
    )


class AuthorEditForm(AuthorBaseForm):
    pass


class AuthorDeleteForm(ReadOnlyMixin, AuthorBaseForm):
    readonly_fields = ['__all__']