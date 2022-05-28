from django.contrib.auth.models import User
from rest_framework import serializers, validators

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'username', 'password')

        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with this email already exists"
                    )
                ]
            },
            'first_name': {
                'required': True,
                'allow_blank': False
            },
            'last_name': {
                'required': True,
                'allow_blank': False
            }
        }

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        # email = validated_data['email']
        # first_name = validated_data['first_name']
        # last_name = validated_data['last_name']
        # username = validated_data['username']
        # password = validated_data['password']

        # user = User.objects.create(
        #     email = email,
        #     first_name = first_name,
        #     last_name = last_name,
        #     username = username,
        #     password = password
        # )

        # return user