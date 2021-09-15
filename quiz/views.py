from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Quizzes
from .serializers import QuizSerializer


class QuizSerializer(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()
