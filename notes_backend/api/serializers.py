from rest_framework import serializers
from .models import Note

# PUBLIC_INTERFACE
class NoteSerializer(serializers.ModelSerializer):
    """Serializes Note objects for API responses and writes."""

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
