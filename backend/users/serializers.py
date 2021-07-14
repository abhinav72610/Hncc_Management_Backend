from rest_framework import serializers
from users.models import NewUser, Profile


# from drf_writable_nested import WritableNestedModelSerializer


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('id', 'email', 'user_name', 'password', 'year')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     kwargs['partial'] = True
    #     super(ProfileSerializer, self).__init__(*args, **kwargs)

    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'github_username',
                  'codechef_username', 'expertise']


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = NewUser
        fields = ['token']
