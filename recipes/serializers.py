from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'ingredients', 'instructions', 'image',
            'tags', 'author', 'created_at', 'updated_at',
            'prep_time', 'cook_time', 'servings', 'difficulty', 'cuisine',
            'source_url', 'video_url', 'notes', 'featured'
        ]