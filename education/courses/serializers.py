from rest_framework import serializers

from .models import Lesson, UserAvailableProduct, UserProgress


class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = '__all__'


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class AvailableProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAvailableProduct
        fields = '__all__'
