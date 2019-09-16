from rest_framework import serializers
from alerts.models import Alert


class AlertSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Alert
        fields = "__all__"