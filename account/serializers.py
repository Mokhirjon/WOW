from .models import Customuser
from rest_framework import serializers

from rest_framework.serializers import ModelSerializer
class Customsirealizers(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta :
        model = Customuser
        fields = ('username','password','role','phone')
    def create(self, validated_data):
        user = Customuser(
        username = validated_data['username'],
        role = validated_data['role'],
        phone = validated_data['phone']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user


