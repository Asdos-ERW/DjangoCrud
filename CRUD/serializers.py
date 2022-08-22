from rest_framework import serializers
from .models import kegiatan

class SerializerKegiatan(serializers.ModelSerializer):
    class Meta: 
        model = kegiatan
        fields = '__all__'