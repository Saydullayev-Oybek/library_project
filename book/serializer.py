from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id' ,'title', 'subtitle', 'author', 'price', 'isbn')

    #
    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError({
                'status': False,
                'message': 'Sarlavha matn kurinishida bulishi kerak'
            })


        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({
                'status': False,
                'message': 'Bunaqa kitob mavjud'
            })
        return data

    def validate_price(self, price):
        if price < 0 or price > 9999999:
            raise ValidationError({
                'status': False,
                'message': 'Notogri miqdordagi narx kiritdingiz'
            })
        return price