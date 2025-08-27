from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ingredients = models.TextField(help_text="List ingredients, separated by new lines.")
    instructions = models.TextField(help_text="List instructions, separated by new lines.")
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, help_text="Comma-separated tags, e.g. 'dessert,vegan'")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    difficulty = models.CharField(max_length=50, choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ])
    prep_time = models.PositiveIntegerField(blank=True, null=True, help_text="Preparation time in minutes")
    cook_time = models.PositiveIntegerField(blank=True, null=True, help_text="Cooking time in minutes")
    servings = models.PositiveIntegerField(blank=True, null=True, help_text="Number of servings")
    difficulty = models.CharField(max_length=10, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], blank=True)
    cuisine = models.CharField(max_length=50, blank=True)
    featured = models.BooleanField(default=False)
    source_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title

class RecipeFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorited_by')
    favorited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.user} favorited {self.recipe}"

class RecipeComment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.recipe}"

class RecipeRating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=1)  # e.g., 1-5 stars
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"Rating: {self.rating} by {self.user} for {self.recipe}"