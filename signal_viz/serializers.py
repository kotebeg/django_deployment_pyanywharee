from rest_framework import serializers


class SignalDataSerializer(serializers.Serializer):
    """Serializes a single data point from the signal DataFrame."""
    time = serializers.IntegerField()
    random_signal = serializers.FloatField(source='Random Signal')


class SignalResponseSerializer(serializers.Serializer):
    """Top-level response wrapper with metadata."""
    num_points = serializers.IntegerField()
    data = SignalDataSerializer(many=True)
