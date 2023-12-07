from rest_framework import serializers
from .models import Student

class StudentSerializier(serializers.Serializer):
    name = serializers.CharField(max_length=50)  
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    # for DeSerializer -----
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    # for Update data --------
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    # Field level Validation----------
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Sorry Seat Full...')
        return value
    
    # Object level Validation----------
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'kaka' and ct.lower() != 'kaka':
            raise serializers.ValidationError('City Must be kaka..')
        return data