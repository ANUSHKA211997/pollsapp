from rest_framework import serializers
from .models import Question,Choice

class QuestionSer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=('question_text','pub_date')

class ChoiceSer(serializers.ModelSerializer):
    class Meta:
        model=Choice
        fields=('choice_text','votes')