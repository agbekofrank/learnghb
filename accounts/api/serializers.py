from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from django.db.models import Q

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label='Email Address')
    email2 = serializers.EmailField(label='Confirm Email')
    class  Meta:
        model = User
        fields = ['username', 'password', 'email','email2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise serializers.ValidationError('Emails Must match!!')
        return value
    def create(self, validated_data):
        print(validated_data)
        username = validated_data['username']
        email = validated_data['email']
        # email2 = validated_data['email2']
        password = validated_data['password']
        user_obj = User(username=username, password=password, email=email)
        user_obj.set_password(password)
        user_obj.save()
        UserLoginSerializer.validate(user_obj, validated_data)
        return validated_data

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(label='Email Address',required=False, allow_blank=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        user_obj = None
        email = data.get('email')
        username = data.get('username')
        password = data['password']
        if not email and not username:
            raise serializers.ValidationError('You need an email or username to login!!')
        user = User.objects.filter(
            Q(username=username)|
            Q(email=email)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError('This username/email is already there!')
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError('Incorrect credentials, try again!!')
        try:
            payload = JWT_PAYLOAD_HANDLER(user_obj)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            # update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        data['token'] = jwt_token
        return data