"""
from rest_framework import serializers
from .models import Login, DataSystem, Notification

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class DataSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSystem
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

    def validate_data_system(self, value):
        if not DataSystem.objects.filter(uuid=value).exists():
            raise serializers.ValidationError("El uuid no existe en el modelo DataSystem")
        return value
"""
from rest_framework import serializers
from .models import Login, DataSystem, Notification


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class DataSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSystem
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['data_system','body','title', 'email']

    def validate_data_system(self, value):
        try:
            DataSystem.objects.get(uuid=value.uuid)
            print(f"HERE --> {value.uuid}")
        except DataSystem.DoesNotExist:
            raise serializers.ValidationError("El UUID no existe en DataSystem.")
        return value
