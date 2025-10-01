from rest_framework import serializers

class EmpSerializer(serializers.Serializer):
    ename=serializers.CharField(max_length=25)
    email=serializers.EmailField()
