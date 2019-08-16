
from rest_framework import serializers
from .models import Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ("sent_to", "sent_from", "body", "subject", "send_date", "archived")
        read_only_fields = ("send_date", "archived")