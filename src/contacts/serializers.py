from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class CreateContactSerializer(ModelSerializer):
    def validate(self, attrs):
        if Contact.objects.filter(phone_number=attrs["phone_number"]).exists():
            raise serializers.ValidationError(
                {"phone_number": ("Phone number is already in use")}
            )
        return super().validate(attrs)

    class Meta:
        model = Contact
        fields = "__all__"
        read_only_fields = ("is_favorite",)
