from regularExam.author.models import Author


def get_author_obj():
    return Author.objects.first()