from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from alerts.models import Alert
from alerts.api.serializers import AlertSerializer


class AlertList(generics.ListAPIView):
    queryset = Aler.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]