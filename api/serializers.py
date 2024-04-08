from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'image', 'location', 'hobby']

    def validate(self, attrs):
        first_name = attrs['first_name']
        last_name = attrs['last_name']
        phone = attrs['phone']

        if len(first_name) < 5 or len(first_name) > 20:
            data = {
                "status": False,
                "message": "Ism kiritishda xatolik",
            }
            return data

        if len(last_name) < 5 or len(last_name) > 20:
            data = {
                "status": False,
                "message": "Familiya kiritishda xatolik",
            }
            return data

        if not phone.startswith("+998") or not phone[4:].isdigit():
            data = {
                "status": False,
                "message": "Telefon raqam kiritishda xatolik",
            }
            return data
        return attrs

    def create(self, validated_data):
        Student.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            image=validated_data['image'],
            location=validated_data['location'],
            hobby=validated_data['hobby'],
        )
        return validated_data

