from rest_framework import serializers
from .models import Follower
from django.db import IntegrityError

class FollowerSerializer(models.ModelSerializer):
    owner = serializers.ReadOnlyField(source='followed.username')


    class Meta:
        model = Follower
        fields = ['id', 'owner', 'created_at', 'followed', 'followed_name']


    def create(self, validated_data):
        try:
            return super().create(validated_data)
            except IntegrityError:
                raise serializers.ValidationError({'detail': 'possible duplicate'})