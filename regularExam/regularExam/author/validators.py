import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class LettersOnlyValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must contain letters only!"
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        pattern = r'^[A-Za-z]+$'

        if not re.match(pattern, value):
            raise ValidationError(self.message)


@deconstructible
class ExactlySixDigitsValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your passcode must be exactly 6 digits!"
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        pattern = r'^\d{6}$'

        if not re.match(pattern, value):
            raise ValidationError(self.message)
