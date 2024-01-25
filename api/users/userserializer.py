from django.contrib.auth.models import User
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    class Meta:
        fields = ['username', 'password']
        
        
        
        
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        account = User(username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account