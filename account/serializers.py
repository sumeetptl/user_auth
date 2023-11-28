from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},
                                    write_only=True)
    class Meta:
        model=User
        fields=["email", "username", "password", "password2"]
        extra_kwargs={
            'password':{'write_only':True}
        }
        
    def validate(self, attrs):
        password= attrs.get("password")
        password2= attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop("password2")
        user=User.objects.create_user(**validated_data)
        return user
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model=User
        fields=["email","password"]
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["id","email","username"]
        
class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']