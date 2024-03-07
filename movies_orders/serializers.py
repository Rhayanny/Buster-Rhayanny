from rest_framework import serializers
from .models import MovieOrder


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    purchased_by = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    purchased_at = serializers.DateTimeField(read_only=True)

    def get_title(self, obj: MovieOrder):
        return obj.movie.title

    def get_purchased_by(self, obj: MovieOrder):
        return obj.user.email

    def create(self, validated_data) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
