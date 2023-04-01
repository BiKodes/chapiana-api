from rest_framework import serializers

from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if User.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError({"email": ("Email is already in use")})
        return super().validate(attrs)

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("auth_token",)
        extra_kwargs = {"password": {"write_only": True}}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ="__all__"
        read_only_fields = ("username",)
