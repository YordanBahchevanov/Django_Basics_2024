from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# def bad_language_validator(value):
#     bad_words = ["bad_word1", "bad_word2", "bad_word3"]
#
#     for bad_word in bad_words:
#
#         if bad_word.lower() in value.lower():
#             raise ValidationError('The text contains bad language!')


@deconstructible
class BadLanguageValidator:

    def __init__(self, bad_words=None):
        if bad_words is None:
            self.bad_words = ["Bad_word1", "bad_word2", "bad_word3"]
        else:
            self.bad_words = bad_words

    @property
    def bad_words(self):
        return self._bad_words

    @bad_words.setter
    def bad_words(self, new_words):
        if not isinstance(new_words, list):
            raise TypeError("bad_words must be a list")
        self._bad_words = [word.lower() for word in new_words]

    def __call__(self, value):
        for bad_word in self.bad_words:
            if bad_word in value.lower():
                raise ValidationError('The text contains bad language!')


# validator = BadLanguageValidator()
# print(validator.bad_words)
#
# validator.bad_words = ['new_Bad_word', 'NeW_bad_word2']
# print(validator.bad_words)
#
# try:
#     validator("This contains new_bad_word.")
# except ValidationError as e:
#     print(e)
