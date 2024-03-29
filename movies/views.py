from rest_framework.views import Response, status, Request, APIView
from .serializers import MovieSerializer, CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsEmployee
from .models import Movie
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class MoviesView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    def post(self, request: Request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        movie = self.paginate_queryset(Movie.objects.all(), request)
        seriliazer = MovieSerializer(movie, many=True)

        return self.get_paginated_response(seriliazer.data)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    def get(self, request: Request, movie_id) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
