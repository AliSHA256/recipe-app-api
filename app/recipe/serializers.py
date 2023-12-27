"""
Serializers for recipe APIs.
"""
from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializers for recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'link', 'time_minutes', 'price']
        read_only_fields = ['id']


class RecipeDetailsSerializer(RecipeSerializer):
    """
    Serializer for recipes detail view.
    """

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
