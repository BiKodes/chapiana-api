from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Contact

class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ['owner' ,'contact_image', 'first_name', 'last_name', 'country_code', 'phone_number', 
                    'is_favorite']


class CreateContactSerializer(ModelSerializer):

    def validate(self, attrs):
        if Contact.objects.filter(phone_number=attrs['phone_number']).exists():
            raise serializers.ValidationError(
                {'phone_number': ('Phone number is already in use')}
            )
        return super().validate(attrs)

    # def create(self, validated_data):
    #     contact = Contact.objects.create(**validated_data)
    #     return contact

    # def update(self, validated_data):
    #     contact = Contact.objects.update(**validated_data)
    #     return contact

    class Meta:
        model = Contact
        fields = ('id', 'owner', 'contact_image', 'first_name', 'last_name', 'phone_number', 'country_code',)
        read_only_fields = ('is_favorite',)