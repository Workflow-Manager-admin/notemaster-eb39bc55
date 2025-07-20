from django.db import models

# PUBLIC_INTERFACE
class Note(models.Model):
    """Model representing a Note."""
    title = models.CharField(max_length=200, db_index=True, help_text="The note's title.")
    content = models.TextField(blank=True, help_text="The note's content.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the note was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the note was last updated.")

    def __str__(self):
        return self.title
