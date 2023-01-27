from rest_framework.serializers import FileField, Serializer
from .models import DataPost


class DataPostSerializer(Serializer):
    upload = FileField(read_only=True)

    class Meta:
        models = DataPost
        fields = "__all__"
