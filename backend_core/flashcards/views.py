from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import FlashCard
from .serializers import FlashCardSerializer


class FlashCardView(ListAPIView):
    serializer_class = FlashCardSerializer

    def get_queryset(self):

        rating = self.kwargs.get('rating', 0)

        return FlashCard.objects.filter(rating__gte=rating)


class FlashCardItemView(RetrieveUpdateDestroyAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer


class FlashCardCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlashCardSerializer



