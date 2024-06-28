from rest_framework import serializers

class PredictRequestSerializer(serializers.Serializer):
    url = serializers.URLField()
