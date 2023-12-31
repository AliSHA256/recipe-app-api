"""
Serializers for recipe APIs.
"""
from rest_framework import serializers
from core.models import (
    Recipe,
    Tag,
    Ingredient,
)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredient."""
    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ['id']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    """Serializers for recipes."""

    tags = TagSerializer(many=True, required=False)
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'link', 'time_minutes',
                  'price', 'tags', 'ingredients',]
        read_only_fields = ['id']

    def _get_or_create_tags(self, tags, recipe):
        """Getting or creating tags."""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            recipe.tags.add(tag_obj)

    
    def _get_or_create_ingredient(self, ingredients, recipe):
        """Getting and creating ingredients."""
        auth_user = self.context['request'].user
        for ingredient in ingredients:
            ingredient_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **ingredient,
            )
            recipe.ingredient.add(ingredient_obj)
        

    def create(self, validated_data):
        """Create a recipe."""
        tags = validated_data.pop('tags', [])
        ingredients = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)
        self._get_or_create_tags(ingredients, recipe)
        return recipe

    def update(self, instance, validated_data):
        """Update a recipe."""
        tags = validated_data.pop('tags', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance


class RecipeDetailsSerializer(RecipeSerializer):
    """
    Serializer for recipes detail view.
    """

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
