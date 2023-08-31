from rest_framework import generics
from .models import Week
from .serializers import WeekSerializers
# Create your views here.

class WeekAllget(generics.ListAPIView):
    queryset=Week.objects.all()
    serializer_class = WeekSerializers

class WeekUpdate(generics.CreateAPIView):
    queryset=Week.objects.all()
    serializer_class = WeekSerializers
class WeekDeeteles(generics.RetrieveAPIView):
    queryset=Week.objects.all()
    serializer_class = WeekSerializers
class Weekdelete(generics.DestroyAPIView):
    queryset=Week.objects.all()
    serializer_class = WeekSerializers
