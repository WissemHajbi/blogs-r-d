from rest_framework.serializers import ModelSerializer
from blogs.models import blog

class blogSerializer(ModelSerializer):
    class Meta:
        model = blog
        fields = "__all__"
        
