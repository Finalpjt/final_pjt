from rest_framework import serializers
from .models import Accounts
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['username', 'email', 'nickname', 'profile_img'] 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['nickname', 'email', 'profile_img'] 
        # exclude = ['username', 'password', 'followings']

class UserNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['id', 'nickname']


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, max_length=150)
    # profile_img = serializers.ImageField(use_url=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        # data['profile_img'] = self.validated_data.get('profile_img','')
        return data