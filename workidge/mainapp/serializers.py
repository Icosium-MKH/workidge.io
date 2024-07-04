from rest_framework import serializers
from .models import Competence,Developer

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = ['name']


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['id', 'name', 'surname', 'email', 'pn', 'title', 'skills']