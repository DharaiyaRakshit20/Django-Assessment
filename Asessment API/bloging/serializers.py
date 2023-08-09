# from rest_framework import serializers
# from .models import *

# class formserial(serializers.Modelserializers):
#     class Meta:
#         model= form
#         filds= '__all__'

from rest_framework import serializers
from .models import *

class formSerializer(serializers.ModelSerializer):
    class Meta:
        model = form
        fields = '__all__'
