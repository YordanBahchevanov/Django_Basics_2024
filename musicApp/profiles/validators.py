from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class AlphaNumericValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Ensure this value contains only letters, numbers, and underscore."
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if "-" in value or value.lower() != slugify(value):
            raise ValidationError(self.message)

    # def __call__(self, value: str, *args, **kwargs):
    #     # Regex pattern to allow only letters, numbers, and underscores
    #     pattern = r'^[\w]+$'  # \w matches [a-zA-Z0-9_]
    #
    #     if not re.match(pattern, value):
    #         raise ValidationError(self.message)