from rest_framework import serializers
from .models import User, Product

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create_user(self, validated_data):
        password = validated_data.pop('password', None) #popped out so it will not be in the instance model
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        # instance.is_active=True
        instance.save()
        return instance