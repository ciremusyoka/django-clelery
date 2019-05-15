from rest_framework import serializers

from .models import Example

class AnsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = '__all__'