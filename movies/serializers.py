from rest_framework import serializers
from .models import Movie
from .models import Rating
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default="", allow_null=True)
    rating = serializers.ChoiceField(choices=Rating.choices, default=Rating.G)
    synopsis = serializers.CharField(default="", required=False, allow_null=True)
    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.rating = validated_data.get("rating", instance.rating)
        instance.synopsis = validated_data.get("synopsis", instance.synopsis)
        instance.save()
        return instance
