from rest_framework.serializers import ModelSerializer

from .models import FlashCard, Deck


class FlashCardSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('id', 'question', 'answer', 'decks', 'author', 'category', 'difficulty', 'rating', 'tags')


class DeckSerializer(ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'name', 'author', 'category', 'difficulty', 'rating', 'tags', 'description', 'is_public')
