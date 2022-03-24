from rest_framework.serializers import Serializer
from .models import User


class UserSerializer(Serializer.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"