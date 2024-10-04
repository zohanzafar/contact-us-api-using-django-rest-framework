from rest_framework import serializers
from .models import Contact
import re

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("First name must only contain alphabetic characters.")
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Last name must only contain alphabetic characters.")
        return value

    def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError("Email must contain '@'.")
        if not value.endswith(('.com', '.org', '.net')):
            raise serializers.ValidationError("Invalid email domain. Accepted domains are .com, .org, .net.")
        return value


    def validate_phone(self, value):
        phone_pattern = r'^\+?1?\d{9,15}$'
        if not re.match(phone_pattern, value):
            raise serializers.ValidationError("Phone number must be in a valid international format.")
        return value

    def validate_message(self, value):
        if not (10 <= len(value) <= 255):
            raise serializers.ValidationError("Message should be between 10 and 255 characters long.")
        return value

