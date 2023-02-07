from rest_framework import serializers
from ..models.booking import Booking


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'title', 'description', 'completed')
