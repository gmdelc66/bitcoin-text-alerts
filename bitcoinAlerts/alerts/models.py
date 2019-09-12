from django.db import models
from django.contrib.auth import get_user_model


class Alerts(models.Model):
    user_id = models.ForeignKey(get_user_model(),
                                on_delete=models.CASCADE,
                                )
    quote = models.CharField(max_length=128)
    base = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()
    send_count = models.PositiveIntegerField()
