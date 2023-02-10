from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from .models import Deck
from .paginators import CustomPaginator
from .permissions import IsAuthor
from .serializers import DeckSerializer


class DeckViewSet(ModelViewSet):
    queryset = Deck.objects.select_related('difficulty', 'author').prefetch_related('tags').all()
    pagination_class = CustomPaginator
    serializer_class = DeckSerializer

    def list(self, request, *args, **kwargs):
        # serializer = DeckSerializer(self.queryset, many=True)
        # return Response(serializer.data)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, pk=None, **kwargs):
        deck = get_object_or_404(queryset=self.queryset, pk=pk)
        serializer = DeckSerializer(deck)
        return Response(serializer.data)


class DeckOwnerViewSet(ViewSet):
    permission_classes = [IsAuthenticated, IsAuthor]
    queryset = Deck.objects.all()

    def list(self, request):
        decks = self.queryset.filter(author=request.user)
        serializer = DeckSerializer(decks, many=True)
        return Response(serializer.data)

    def retrieve(self,request, pk=None):
        deck = get_object_or_404(queryset=self.queryset, pk=pk)
        self.check_object_permissions(request, deck)
        serializer = DeckSerializer(deck)
        return Response(serializer.data)
