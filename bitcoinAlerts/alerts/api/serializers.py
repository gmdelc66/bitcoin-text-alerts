from rest_framework import serializers
from alerts.models import Alert


class AlertSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Alert
        fields = "__all__"