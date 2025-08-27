from django.contrib import admin
from .models import Recipe, RecipeFavorite, RecipeComment, RecipeRating

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'created_at', 'prep_time', 'cook_time',
        'servings', 'difficulty', 'featured'
    )
    list_filter = ('difficulty', 'featured', 'cuisine', 'tags')
    search_fields = ('title', 'description', 'tags', 'cuisine')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': (
                'title', 'description', 'ingredients', 'instructions', 'image',
                'tags', 'author', 'prep_time', 'cook_time', 'servings', 'difficulty',
                'cuisine', 'source_url', 'video_url', 'notes', 'featured'
            )
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

admin.site.register(RecipeFavorite)
admin.site.register(RecipeComment)
admin.site.register(RecipeRating)