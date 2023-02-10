from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Deck
from .serializers import DeckSerializer


class DeckViewSet(ViewSet):
    queryset = Deck.objects.all()

    def list(self, request):
        serializer = DeckSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        deck = get_object_or_404(queryset=self.queryset, pk=pk)
        serializer = DeckSerializer(deck)
        return Response(serializer.data)
