from django.db.models import fields
from rest_framework import serializers
from.models import Quizzes


class QuizSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]
